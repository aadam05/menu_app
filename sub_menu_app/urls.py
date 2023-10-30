from django.urls import path
from sub_menu_app.views import menu_page
app_name = 'factory_bot'

urlpatterns = [
    path('menu-page/', menu_page, name='menu-page')
]
