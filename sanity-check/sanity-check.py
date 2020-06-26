import os
import re


def read_list_in_directive(file, directive):
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
                    print('ERROR: invalid element in directive \'' + directive + '\' in file: ' + f.name + ' => \'' + line_stripped + '\'')
            if reading_tags and empty_lines < 0:
                return {'file': file, 'array': array}
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
        weird_chars = '‘’´“”–…'
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
        for line in f.readlines():
            line_stripped = line.strip()
            if '.. atf-image::' in line_stripped:
                return {'file': file, 'atf_image_found': True}
        return {'file': file, 'atf_image_found': False}


def check_for_invalid_elements(files, valid_list, element):
    output = [['\nList of the invalid ' + element + 's:\n']]
    for ft in files:
        for elem in ft['array']:
            if elem not in valid_list:
                output.append(['=> Invalid ' + element + ': ' + elem, ft['file'].path])
    print_if_necessary_style_columns(output)


def check_twitter(files):
    output = [['\nList of the Twitter warnings:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        if ':site: @mongodb' not in ft['array']:
            output.append(['=> Missing ":site: @mongodb"', file_path])
        if not any(re.compile(':creator: @.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":creator: @..."', file_path])
        if not any(re.compile(':title:.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":title:"', file_path])
        if not any(re.compile(':image: /images/.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":image:" with relative path', file_path])
        if not any(re.compile(':image-alt:.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":image-alt:"', file_path])
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
    print_if_necessary_style_columns(output)


def check_og(files):
    output = [['\nList of the og warnings:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        if ':type: article' not in ft['array']:
            output.append(['=> Missing ":type: article"', file_path])
        if not any(re.compile(':url:.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":url:"', file_path])
        if not any(re.compile(':title:.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":title:"', file_path])
        if not any(re.compile(':image:.*').match(line) for line in ft['array']):
            output.append(['=> Missing ":image:" with relative path', file_path])
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
    print_if_necessary_style_columns(output)


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
    print_if_necessary_style_columns(output)


def check_links(files):
    output = [['\nList of files missing an underscore in links:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        if ft['link_found']:
            output.append(['=> This file needs some extra underscores.', file_path])
    print_if_necessary_style_columns(output)


def check_type(files):
    output = [['\nList of files with a wrong type:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        type = ft['type']
        if type == '' or (type != ft['folder'] and type not in ['video', 'live']):
            output.append(['=> Type directive is wrong in this file.', file_path])
    print_if_necessary_style_columns(output)


def check_level(files):
    output = [['\nList of files with a wrong level:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        level = ft['level']
        if level == '' or level not in ['beginner', 'intermediate', 'advanced']:
            output.append(['=> Level directive is wrong in this file.', file_path])
    print_if_necessary_style_columns(output)


def check_atf_image(files):
    output = [['\nList of files without directive atf-image:\n']]
    for ft in files:
        file_path = ft['file'].path.replace('../source', '')
        found = ft['atf_image_found']
        if not found:
            output.append(['=> atf-image directive is missing in this file.', file_path])
    print_if_necessary_style_columns(output)


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
    print_if_necessary_style_columns(output)


def print_if_necessary(output):
    if len(output) > 1:
        for line in output:
            print(line)


def print_if_necessary_style_columns(output):
    if len(output) == 1:
        return
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


def check_thing_not_used(things, all_things, things_used):
    output = ['\nList of ' + things + ' not used:\n']
    for thing in all_things:
        if thing not in things_used:
            output.append('=> ' + thing)
    print_if_necessary(output)


def check_thing_not_found(things, all_images, images_used):
    output = ['\nList of ' + things + ' not found:\n']
    for img in images_used:
        if img not in all_images:
            output.append('=> ' + img)
    print_if_necessary(output)


def check_snooty(blog_posts):
    blog_posts = list(map(lambda b: b.path.replace('../source', '').replace('.txt', ''), blog_posts))
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
        print_if_necessary_style_columns(output)


def check_blogs_exist(existing_blog_posts, line, output):
    split = line.split('=')
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

    check_thing_not_used('images', all_images, images_used)
    check_thing_not_found('images', all_images, images_used)

    check_thing_not_used('includes', all_includes, includes_used)
    check_thing_not_found('includes', all_includes, includes_used)
