from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=100, blank=True)
    named_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_children(self):
        return MenuItem.objects.filter(parent=self)

    def has_children(self):
        return MenuItem.objects.filter(parent=self).exists()

    @classmethod
    def get_menu(cls, menu_name):
        menu_items = cls.objects.filter(name=menu_name)
        menu = []
        for item in menu_items:
            menu.append(cls._get_menu_item(item))
        return menu

    @classmethod
    def _get_menu_item(cls, item):
        menu_item = {
            'name': item.name,
            'url': item.url,
            'named_url': item.named_url,
            'children': []
        }
        children = item.get_children()
        if children:
            for child in children:
                menu_item['children'].append(cls._get_menu_item(child))
        return menu_item


