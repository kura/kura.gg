"""
Extract Table of Content
========================

This plugin allows you to extract table of contents (ToC) from article.content
and place it in its own article.toc variable.
"""

from os import path
from bs4 import BeautifulSoup
from pelican import signals, readers, contents


def extract_toc(content):
    if isinstance(content, contents.Static):
        return
    soup = BeautifulSoup(content._content,'html.parser')
    filename = content.source_path
    extension = path.splitext(filename)[1][1:]
    toc = ''
    # if it is a Markdown file
    if extension in readers.MarkdownReader.file_extensions:
        toc = soup.find('div', class_='toc')
    # else if it is a reST file
    elif extension in readers.RstReader.file_extensions:
        toc = soup.find('div', class_='contents topic')
    if toc:
        toc.extract()
        content._content = soup.decode()
        keep_header = content.settings.get('TOC_HEADER', False)
        if keep_header is True:
            content.toc = toc.decode()
        else:
            content.toc = '\n'.join(toc.decode().split('\n')[2:-1])


def register():
    signals.content_object_init.connect(extract_toc)
