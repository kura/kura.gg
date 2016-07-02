import base64
import os


BASE_PATH = '/home/kura/workspace/kura.io/eevee/static/'
CSS_PATH = os.path.join(BASE_PATH, 'css')
FONTS_PATH = os.path.join(BASE_PATH, 'fonts')
FONT_FACE = {
'firasans-light': """@font-face {{
    font-family: 'FiraSans';
    font-style: normal;
    font-weight: 300;
    src: {},
         {};
}}""",
'firasans-regular': """@font-face {{
    font-family: 'FiraSans';
    font-style: normal;
    font-weight: 400;
    src: {},
         {};
}}""",
'firasans-semibold': """@font-face {{
    font-family: 'FiraSans';
    font-style: normal;
    font-weight: 600;
    src: {},
         {};
}}""",
'firasans-bold': """@font-face {{
    font-family: 'FiraSans';
    font-style: normal;
    font-weight: 700;
    src: {},
         {};
}}""",
'firamono-regular': """@font-face {{
    font-family: 'FiraMono';
    font-style: normal;
    font-weight: 400;
    src: {},
         {};
}}""",
'roboto-light': """@font-face {{
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 300;
    src: {},
         {};
}}""",
'roboto-regular': """@font-face {{
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    src: {},
         {};
}}""",
'roboto-medium': """@font-face {{
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 500;
    src: {},
         {};
}}""",
'roboto-bold': """@font-face {{
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    src: {},
         {};
}}""",
'fontawesome': """@font-face {{
    font-family: 'FontAwesome';
    font-weight: normal;
    font-style: normal;
    src: {},
         {};
}}""",
'materialicons-regular': """@font-face {{
  font-family: 'Material Icons';
  font-style: normal;
  font-weight: 400;
  src: {},
       {};
}}"""
}


def encode(font, ext):
    font_file = '{}.{}'.format(font, ext)
    font_path = os.path.join(FONTS_PATH, font_file)
    font_content = open(font_path, 'rb').read()
    return base64.b64encode(font_content).decode('utf-8')

with open(os.path.join(CSS_PATH, 'fonts.css'), 'w') as css_file:
    for font in sorted(os.listdir(FONTS_PATH)):
        if 'roboto' not in font and 'woff2' in font:
            font_name = font.split('.', 1)[0]
            print(font_name)
            woff2 = "url('data:font/woff2;base64,{}') format('woff2')".format(encode(font_name, 'woff2'))
            woff = "url('data:font/woff;base64,{}') format('woff')".format(encode(font_name, 'woff'))
            svg = "url('data:application/x-font-svg;base64,{}') format('svg')".format(encode(font_name, 'svg'))
            css_font_face = FONT_FACE[font_name]
            css = css_font_face.format(woff2, woff)
            css_file.write('{}\n'.format(css))
