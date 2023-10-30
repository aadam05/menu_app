from django import template
from django.utils.html import format_html
from sub_menu_app.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.get_menu(menu_name)
    if menu:
        return format_html(render_menu(menu))
    return ""


def render_menu(menu_item):
    menu_html = ""
    for item in menu_item:
        menu_html += "<ul class='menu'>"
        menu_html += f"<li><a href='{ item['url'] }'>{ item['name'] }</a>"
        if item['children']:
            menu_html += render_menu(item['children'])
        menu_html += "</li>"
        menu_html += "</ul>"
    return menu_html
