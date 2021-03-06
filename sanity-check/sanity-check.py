import os
import re

from PIL import Image

# Set the exit code to 0 by default to indicate a clean exit
exit_code = 0


def read_list_in_directive(file, directive):
    output = [['\nERROR: invalid element in directive:\n']]
    with open(file.path, encoding='utf-8') as f:
        reading_tags = False
        empty_lines = 1
        array = []
        for line in f.readlines():
            line_stripped = line.strip()
            if directive in line:
                reading_tags = True
            if reading_tags and '' == line_stripped:
                empty_lines -= 1
            if reading_tags and empty_lines == 0 and '' != line_stripped:
                try:
                    array.append(line.split('*')[1].strip())
                except:
                    output.append(directive + '\' in file: ' + f.name + ' => \'' + line_stripped + '\'')
            if reading_tags and empty_lines < 0:
                return {'file': file, 'array': array}
        handle_errors(output, False)
        return {'file': file, 'array': array}


def read_directive(file, directive):
    with open(file.path, encoding='utf-8') as f:
        reading_directive = False
        empty_lines = 1
        array = []
        description = ''
        for line in f.readlines():
            line_stripped = line.strip()
            if directive in line:
                reading_directive = True
            if reading_directive and '' == line_stripped and empty_lines <= 0:
                return {'file': file, 'array': array, 'description': description}
            if reading_directive and '' != line_stripped and empty_lines == 1:
                array.append(line_stripped)
            if reading_directive and '' == line_stripped:
                empty_lines -= 1
            if reading_directive and '' != line_stripped and empty_lines == 0:
                description = line_stripped
        return {'file': file, 'array': array, 'description': description}


def read_type_directive(file):
    with open(file.path, encoding="utf-8") as f:
        path_split = file.path.replace('\\', '/').split('/')
        for line in f.readlines():
            line_stripped = line.strip()
            if '.. type::' in line_stripped:
                return {'file': file, 'type': line_stripped.split()[2] if len(line_stripped.split()) >= 3 else '', 'folder': path_split[2]}
        return {'file': file, 'folder': path_split[2]}


def read_weird_characters(file):
    with open(file.path, encoding='utf-8') as f:
        weird_chars = '‘’´“”…'
        regex = r'[' + weird_chars + '].*[' + weird_chars + ']?'
        lines = []
        for line_nb, line in enumerate(f.readlines()):
            if any(x in line for x in weird_chars):
                search = re.search(regex, line)
                lines.append('l.' + str(line_nb + 1) + ': ' + str.strip(line[search.start():search.end()]))
        return {'file': file, 'lines': lines, 'chars': weird_chars}


def read_level_directive(file):
    with open(file.path, encoding='utf-8') as f:
        for line in f.readlines():
            line_stripped = line.strip()
            if '.. level::' in line_stripped:
                return {'file': file, 'level': line_stripped.split()[2]}
        return {'file': file}


def read_meta_description_directive(file):
    with open(file.path, encoding='utf-8') as f:
        reading_directive = False
        empty_lines = 1
        description = ''
        for line in f.readlines():
            line_stripped = line.strip()
            if '.. meta-description' in line:
                reading_directive = True
            if reading_directive and '' == line_stripped:
                empty_lines -= 1
            if reading_directive and empty_lines == 0 and '' != line_stripped:
                description = line_stripped
            if reading_directive and empty_lines < 0:
                return {'file': file, 'description': description}
        return {'file': file, 'description': description}


def read_links(file):
    with open(file.path, encoding='utf-8') as f:
        for line in f.readlines():
            if re.match(r".*>`_[^_].*", line):
                return {'file': file, 'link_found': True}
        return {'file': file, 'link_found': False}


def read_atf_image(file):
    with open(file.path, encoding='utf-8') as f:
        for index, line in enumerate(f.readlines()):
            line_stripped = line.strip()
            if '.. atf-image::' in line_stripped:
                image = re.findall('/images/.*', line_stripped)
                if len(image) == 1:
                    im = Image.open(os.path.join('../source/', image[0][1:]))
                    width, height = im.size
                    return {'file': file, 'atf_image_found': True, 'line_number': index, 'size': True, 'width': width, 'height': height, 'image': image[0]}
                else:
                    return {'file': file, 'atf_image_found': True, 'line_number': index, 'size': False}
        return {'file': file, 'atf_image_found': False}


def check_for_invalid_elements(files, valid_list, element):
    output = [['\nList of the invalid ' + element + 's:\n']]
    for ft in files:
        for elem in ft['array']:
            if elem not in valid_list:
                output.append(['=> Invalid ' + element + ': ' + elem, ft['file'].path])
    handle_errors(output, True)


def check_twitter(files):
    output = [['\nList of the Twitter warnings:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        if not any(re.compile(':creator: @.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":creator: @..."', file_path])
        if not any(re.compile(':title:.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":title:"', file_path])
        if not any(re.compile(':image: /images/.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":image:" with relative path', file_path])
        if not any(re.compile(':image-alt:.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":image-alt:"', file_path])
        if any(re.compile(':site:.*').match(line) for line in ft['array']):
            output.append(['=> :site: is populated automatically. Just remove it.', file_path])
        description = ft['description']
        length_desc = len(description)
        if length_desc > 160:
            output.append(['=> Description too long (160 max) - need to remove ' + str(length_desc - 160) + ' characters', file_path])
        if length_desc == 0:
            output.append(['=> Description is empty.', file_path])
        for line in ft['array']:
            if ':title:' in line:
                title = re.compile(':title:(.*)').search(line).group(1)
                if '' != title and len(title) > 70:
                    output.append(['=> Twitter title is too long (70 max) - need to remove ' + str(len(title) - 70) + ' characters', file_path])
            if ':image:' in line:
                image = re.findall('/images/.*', line)
                if len(image) == 1:
                    try:
                        im = Image.open(os.path.join('../source/', image[0][1:]))
                        width, height = im.size
                        if not close_enough(width, 1024) or not close_enough(height, 512):
                            output.append(['=> Twitter image should be 1024x512. ' + image[0] + ' is ' + str(width) + 'x' + str(height), file_path])
                        if not image[0].startswith('/images/social/twitter/twitter-'):
                            output.append(['=> Twitter image should be in the /images/social/twitter folder and named "twitter-.*". ' + image[0], file_path])
                    except:
                        output.append(['Cannot open image ../source' + image[0], file_path])
                else:
                    output.append(['=> Twitter image is not valid. Impossible to parse.', file_path])
    handle_errors(output, True)


def check_og(files):
    output = [['\nList of the og warnings:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        if not any(re.compile(':title:.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":title:"', file_path])
        if not any(re.compile(':image:.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":image:" with relative path', file_path])
        if any(re.compile(':url: http://.*').match(line) for line in ft['array']):
            output.append(['=> Links in OG URL should always be HTTPS. Remove the URL directive to get the correct one automatically.', file_path])
        if any(re.compile(':type:.*').match(line) for line in ft['array']):
            output.append(['=> :type: is populated automatically. Just delete it.', file_path])
        description = ft['description']
        length_desc = len(description)
        if length_desc > 200:
            output.append(['=> Description too long (200 max) - need to remove ' + str(length_desc - 200) + ' characters', file_path])
        if length_desc == 0:
            output.append(['=> Description is empty.', file_path])
        for line in ft['array']:
            if ':title:' in line:
                title = re.compile(':title:(.*)').search(line).group(1)
                if '' != title and len(title) > 95:
                    output.append(['=> Twitter title is too long (95 max) - need to remove ' + str(len(title) - 95) + ' characters', file_path])
            if ':image:' in line:
                image = re.findall('/images/.*', line)
                if len(image) == 1:
                    try:
                        im = Image.open(os.path.join('../source/', image[0][1:]))
                        width, height = im.size
                        if not close_enough(width, 1200) or not close_enough(height, 630):
                            output.append(['=> OG image should be 1200x630. ' + image[0] + ' is ' + str(width) + 'x' + str(height), file_path])
                        if not image[0].startswith('/images/social/open-graph/og-'):
                            output.append(['=> OG image should be in the /images/social/open-graph folder and named "og-.*". ' + image[0], file_path])
                    except:
                        output.append(['Cannot open image ../source' + image[0], file_path])
                else:
                    output.append(['=> OG image is not valid. Impossible to parse.', file_path])
    handle_errors(output, True)


def check_meta_description(files):
    output = [['\nList of the Meta Description warnings:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        description = ft['description']
        length_desc = len(description)
        if length_desc == 0:
            output.append(['=> Description is empty.', file_path])
        if length_desc > 155:
            output.append(['=> meta-description is too long (155 characters max) - need to remove ' + str(length_desc - 155) + ' characters', file_path])
    handle_errors(output, True)


def check_links(files):
    output = [['\nList of files missing an underscore in links:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        if ft['link_found']:
            output.append(['=> This file needs some extra underscores.', file_path])
    handle_errors(output, True)


def check_type(files):
    output = [['\nList of files with a wrong type:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        type = ft['type']
        if type == '' or (type != ft['folder'] and type not in ['video', 'live']):
            output.append(['=> Type directive is wrong in this file.', file_path])
    handle_errors(output, True)


def check_level(files):
    output = [['\nList of files with a wrong level:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        level = ft['level']
        if level == '' or level not in ['beginner', 'intermediate', 'advanced']:
            output.append(['=> Level directive is wrong in this file.', file_path])
    handle_errors(output, True)


def check_atf_image(files):
    output = [['\nList of files with directive atf-image problems:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        found = ft['atf_image_found']
        line_number = ft.get('line_number')
        size = ft.get('size')
        width = ft.get('width')
        height = ft.get('height')
        image = ft.get('image')
        if not found:
            output.append(['=> atf-image directive is missing in this file.', file_path])
        if line_number != 2:
            output.append(['=> atf-image directive is not on line 3 in this file.', file_path])
        if not image.startswith('/images/atf-images/'):
            output.append(['=> atf-images should be in the /images/atf-images/ folder.', file_path])
        if not size:
            output.append(['=> atf-image: impossible check the size of the image.', file_path])
        else:
            squared = close_enough(width, height)
            if not squared or width <= 299:
                output.append(['=> atf-image: image is not 360x360 or 720x720. Actual size: ' + str(width) + 'x' + str(height), file_path])
    handle_errors(output, True)


def close_enough(a, b):
    return abs(a - b) <= 1


def check_weird_characters(files):
    output = [['\nList of files with weird characters:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        lines = ft['lines']
        chars = ft['chars']
        if len(lines) != 0:
            output.append(['=> this file contains weird characters like ' + chars, file_path])
            for line in lines:
                output.append(['  - ' + str.strip(line[:70])])
    handle_errors(output, True)


# If no output is passed, the method assumes there are no errors
def handle_errors(output, should_print_column_style_output):
    # if the length of the output is less than or equal to 1, we have no errors to handle
    if len(output) <= 1:
        return

    # set the exit code to 1 to indicate we have an error
    global exit_code
    exit_code = 1

    # print the output
    if (should_print_column_style_output):
        print(output.pop(0)[0])
        width_col_1 = 0
        width_col_2 = 0
        for i in range(len(output)):
            width_col_1 = max(width_col_1, len(output[i][0]))
            if len(output[i]) > 1:
                width_col_2 = max(width_col_2, len(output[i][1]))
        for i in range(len(output)):
            if len(output[i]) > 1:
                print(output[i][0].ljust(width_col_1), ' => ', output[i][1].ljust(width_col_2))
            else:
                print(output[i][0].ljust(width_col_1))
    else:
        for line in output:
            print(line)


def scan_images(file):
    with open(file, encoding='utf-8') as f:
        images = []
        for line in f.readlines():
            line_chards = line.split()
            for chard in line_chards:
                if chard.startswith('/images/'):
                    images.append(chard)
        return images


def scan_includes(file):
    with open(file, encoding='utf-8') as f:
        includes = []
        for line in f.readlines():
            if line.strip().startswith('.. include::'):
                includes.append(line.strip().split()[2])
        return includes


def check_thing_not_used(things, all_things, things_used, things_to_ignore):
    output = ['\nList of ' + things + ' not used:\n']
    for thing in all_things:
        if not thing.endswith(".DS_Store"):
            if thing not in things_used:
                if things_to_ignore is not None:
                    if thing not in things_to_ignore:
                        output.append('=> ' + thing)
                else:
                    output.append('=> ' + thing)
    handle_errors(output, False)


def check_thing_not_found(things, all_images, images_used):
    output = ['\nList of ' + things + ' not found:\n']
    for img in images_used:
        if img not in all_images:
            output.append('=> ' + img)
    handle_errors(output, False)


def check_snooty(blog_posts):
    blog_posts = list(map(lambda b: b.path.replace('../source', '').replace('.txt', '/').replace('\\', '/'), blog_posts))
    output = [['\nList of errors in snooty.toml.\n']]
    with open('../snooty.toml', encoding='utf-8') as f:
        home = ''
        learn = ''
        reading_page_groups = False
        page_groups = []
        for line in f.read().splitlines():
            line = line.strip()
            if line.startswith('"home"'):
                home = line
            if line.startswith('"learn"'):
                learn = line
            if line == '[page_groups]':
                reading_page_groups = True
            if reading_page_groups and line == '':
                reading_page_groups = False
            if reading_page_groups and line != '[page_groups]':
                page_groups.append(line)
        if home == '':
            output.append(['=> ERROR: Featured articles for the "home" page are missing in "snooty.toml".'])
        if learn == '':
            output.append(['=> ERROR: Featured articles for the "learn" page are missing in "snooty.toml".'])
        for line in page_groups:
            check_blogs_exist(blog_posts, line, output)
        handle_errors(output, True)


def check_blogs_exist(existing_blog_posts, line, output):
    # Split from the right side on the equals sign. This assumes the blog urls have no equal signs
    split = line.rsplit('=', 1)
    snooty_part = split[0]
    blog_posts_in_line = eval(split[1])
    imaginary_blog_posts = set(blog_posts_in_line) - set(existing_blog_posts)
    for blog in imaginary_blog_posts:
        output.append(['=> This blog post does not exist in ' + snooty_part, blog])


if __name__ == '__main__':
    with open('tags.txt', encoding='utf-8') as f:
        valid_tags = f.read().splitlines()
    with open('products.txt', encoding='utf-8') as f:
        valid_products = f.read().splitlines()
    with open('languages.txt', encoding='utf-8') as f:
        valid_languages = f.read().splitlines()
    with open('ignored-images.txt', encoding='utf-8') as f:
        ignored_images = f.read().splitlines()

    blog_posts = []
    with os.scandir('../source/article') as f:
        for file in filter(lambda x: x.path.endswith(".txt"), f):
            blog_posts.append(file)
    with os.scandir('../source/how-to') as f:
        for file in filter(lambda x: x.path.endswith(".txt"), f):
            blog_posts.append(file)
    with os.scandir('../source/quickstart') as f:
        for file in filter(lambda x: x.path.endswith(".txt"), f):
            blog_posts.append(file)
    with os.scandir('../source/community') as f:
        for file in f:
            blog_posts.append(file)
    file_tags = []
    file_products = []
    file_languages = []
    file_twitter = []
    file_meta_description = []
    file_links = []
    file_og = []
    file_type = []
    file_level = []
    file_atf_image = []
    file_weird_characters = []
    images_used = set()
    includes_used = set()

    for file in blog_posts:
        file_tags.append(read_list_in_directive(file, '.. tags::'))
        file_products.append(read_list_in_directive(file, '.. products::'))
        file_languages.append(read_list_in_directive(file, '.. languages::'))
        file_twitter.append(read_directive(file, '.. twitter::'))
        file_og.append(read_directive(file, '.. og::'))
        file_meta_description.append(read_meta_description_directive(file))
        file_links.append(read_links(file))
        file_type.append(read_type_directive(file))
        file_level.append(read_level_directive(file))
        file_atf_image.append(read_atf_image(file))
        file_weird_characters.append(read_weird_characters(file))

    check_snooty(blog_posts)
    check_for_invalid_elements(file_tags, valid_tags, 'tag')
    check_for_invalid_elements(file_products, valid_products, 'product')
    check_for_invalid_elements(file_languages, valid_languages, 'language')
    check_twitter(file_twitter)
    check_og(file_og)
    check_meta_description(file_meta_description)
    check_links(file_links)
    check_type(file_type)
    check_level(file_level)
    check_atf_image(file_atf_image)
    check_weird_characters(file_weird_characters)

    blog_posts_and_authors = list(blog_posts)

    with os.scandir('../source/includes/authors') as f:
        for file in filter(lambda x: x.path.endswith(".rst"), f):
            blog_posts_and_authors.append(file)

    for file in blog_posts_and_authors:
        images_used.update(scan_images(file))
        includes_used.update(scan_includes(file))

    all_images = []
    for (dirpath, dirnames, filenames) in os.walk('../source/images'):
        all_images += [os.path.join(dirpath, file).replace('../source', '').replace('\\', '/') for file in filenames if not file.endswith('.DS_STORE')]

    all_includes = []
    for (dirpath, dirnames, filenames) in os.walk('../source/includes'):
        all_includes += [os.path.join(dirpath, file).replace('../source', '').replace('\\', '/') for file in filenames if not file.endswith('.DS_STORE')]

    check_thing_not_used('images', all_images, images_used, ignored_images)
    check_thing_not_found('images', all_images, images_used)

    check_thing_not_used('includes', all_includes, includes_used, None)
    check_thing_not_found('includes', all_includes, includes_used)

    print("Sanity check is complete")

    exit(exit_code)
