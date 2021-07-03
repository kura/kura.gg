import logging
import re

from pelican import contents, signals

log = logging.getLogger(__name__)

ERT_WPM = 200  # words per minute by default
ERT_FORMAT = '{time} read'
ERT_INT = False


def initialize(gen):
    global ERT_WPM, ERT_FORMAT
    for option in ['ERT_WPM', 'ERT_FORMAT', 'ERT_INT']:
        if not option in gen.settings.keys():
            log.warning(
                'The necessary config option is missing: {},\
 using default value: \'{}\''.format(option, globals()[option])
            )
        else:
            globals()[option] = gen.settings[option]


def strip_tags(content):
    return re.sub(u'<!--.*?-->|<[^>]*>', '', content)


def estimate(text):
    minutes = len(strip_tags(text).split()) / ERT_WPM
    if minutes < 1:
        time = '< 1 min'
    elif minutes < 60:
        rounded = round(minutes)
        if ERT_INT :
            rounded = int(rounded)
        time = '{} min'.format(rounded)
    else:
        if time // 60 == 1:
            end = ''
        else:
            end = 's'

        rounded_minutes = round(minutes // 60)
        rounded_hours = round(minutes - rounded_minutes * 60)

        if ERT_INT:
            rounded_minutes = int(rounded_minutes)
            rounded_hours = int(rounded_hours)

        time = '{} hour{} {} min'.format(
            rounded_minutes,
            end,
            rounded_hours 
        )
    return ERT_FORMAT.format(time=time)


def ert(obj):
    if obj._content:
        obj.ert = estimate(obj._content)


def register():
    signals.article_generator_init.connect(initialize)
    signals.content_object_init.connect(ert)
