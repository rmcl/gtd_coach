from django import template
from django.utils.html import escape

register = template.Library()


@register.tag(name="display_code")
def do_display_code(parser, token):
    nodelist = parser.parse(('end_display_code',))
    parser.delete_first_token()
    return DisplayCodeNode(nodelist)


class DisplayCodeNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return escape(output)
