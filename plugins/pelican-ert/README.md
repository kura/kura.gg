pelican-ert plugin
====================

A plugin for estimating time that could be spent for an article reading.
------------------------------------------------------------------------
# How it works

## Required configuration

### Description of the variables
Your pelicanconf.py should include following new options:
- **ERT_WPM**: number of words that human usually read per one minute
- **ERT_FORMAT**: format string, that contains `{time}` entry.
- **ERT_INT** `True` or `False` whether or not the time displays as an integer
    or a float

### Default configuration
```
ERT_WPM = 200
ERT_FORMAT = '{time} read'
```

## Accessing the estimated reading time information
For example, this is the code from my `article.html` template:
```
{% if article.ert %} <strong>{{ article.ert }} </strong> {% endif %}
```
![Screenshot](https://raw.githubusercontent.com/nogaems/pelican-ert/screenshot/screenshot.png)
i.e. feel free to use it in any place where you have an access to `article` entity.
