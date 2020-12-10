import os


def scan_publication_dates(file):
    with open(file.path, encoding='utf-8') as f:
        for l in f.readlines():
            if '.. pubdate::' in l:
                return file.path.replace('\\', '/').replace('../source', ''), l.replace('.. pubdate::', '').strip()


if __name__ == '__main__':
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

    publication_dates = []
    for file in blog_posts:
        publication_dates.append(scan_publication_dates(file))

    publication_dates = sorted(publication_dates, key=lambda x: x[1], reverse=True)
    home = str([p.replace('.txt', '/') for p, d in publication_dates[:4]]).replace('\'', '"')
    learn = str([p.replace('.txt', '/') for p, d in publication_dates[4:7]]).replace('\'', '"')

    with open('../snooty.toml', encoding='utf-8') as f:
        lines = f.readlines()
    with open('../snooty.toml', 'w', encoding='utf-8') as f:
        for line in lines:
            if line.startswith('"home"'):
                f.write('"home" = ' + home + '\n')
            elif line.startswith('"learn"'):
                f.write('"learn" = ' + learn + '\n')
            else:
                f.write(line)

    print('Job Done. Check your git status.')
