from django.urls import resolve
from sub_menu_app.models import MenuItem


def active_menu(request):
    current_url = resolve(request.path_info)
    menu_item = MenuItem.objects.filter(url=request.path_info).first()
    return {'active_menu': menu_item}
