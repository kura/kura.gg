from pelican import readers
from pelican.readers import PelicanHTMLTranslator
from pelican import signals
from docutils import nodes

LINK_CHAR = '*'


def init_headerid(sender):
    global LINK_CHAR
    char = sender.settings.get('HEADERID_LINK_CHAR')
    if char:
        LINK_CHAR = char


class HeaderIDPatchedPelicanHTMLTranslator(PelicanHTMLTranslator):
    def depart_title(self, node):
        close_tag = self.context[-1]
        parent = node.parent
        if isinstance(parent, nodes.section) and parent.hasattr('ids') and parent['ids']:
            anchor_name = parent['ids'][0]
            # add permalink anchor
            if close_tag.startswith('</h'):
                html = ('<a class="headerlink" href="#{}" title="Permalink to '
                        'this headline">{}</a>').format(anchor_name, LINK_CHAR)
                self.body.insert(-1, html)
        PelicanHTMLTranslator.depart_title(self, node)


def register():
    signals.initialized.connect(init_headerid)
    readers.PelicanHTMLTranslator = HeaderIDPatchedPelicanHTMLTranslator
