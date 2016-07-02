#
# 'Cos the touch plugin doesn't work when I publish/rsync for some weird
# reason. Couldn't be bothered to fix it when writing this was quicker.
#


import datetime
import os


def metadata(path, filename):
    rst_file = os.path.join(path, filename)
    date, timestamp, slug = None, None, None
    with open(rst_file) as f:
        for line in f.readlines():
            if line.startswith(':date:'):
                _, date = line.split(' ', 1)
                if date.count(':') > 1:
                    form = '%Y-%m-%d %H:%M:%S'
                else:
                    form = '%Y-%m-%d %H:%M'
                date = date.strip()
                timestamp = datetime.datetime.strptime(date, form).timestamp()
            if line.startswith(':slug:'):
                slug = line.split(' ')[1].strip()
        return date, timestamp, slug


def html_file(date, filename):
    year, month, day = date.split(' ')[0].split('-')
    return '{}/{}/{}/{}/index.html'.format(year, month, day, filename)


def touch(filename, timestamp):
    path = os.path.join('output', filename)
    print('touching ->', path)
    os.utime(path, (timestamp, timestamp))
    print('touching ->', path.replace('index.html', ''))
    os.utime(path.replace('index.html', ''), (timestamp, timestamp))


def walk(directory):
    for rst_file in os.listdir(directory):
        if not rst_file.endswith('.rst'):
            continue
        date, timestamp, slug = metadata(directory, rst_file)
        html = html_file(date, slug)
        touch(html, timestamp)


walk('content/')
