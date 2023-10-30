from django.shortcuts import render


def menu_page(request):
    context = {
        'menu_name': 'second'
    }
    return render(request, 'menu_page.html', context)
