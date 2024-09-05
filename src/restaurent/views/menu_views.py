from django.shortcuts import render, redirect, get_object_or_404
from restaurent.models.menu import Menu
from restaurent.forms.menu_form import MenuForm


def menu_list(request):
    menus = Menu.objects.all()
    menus_count = Menu.objects.count()
    context = {
            'menus': menus,
            'menus_count': menus_count
               }
    return render(request, 'menu/menu.html', context)

def menu_form(request, id=None):
    if id:
        menu = get_object_or_404(Menu, id=id)
        form_title = "Modifier le menu"
    else:
        plat = None
        form_title = "Ajouter un menu"
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('restaurent:menu_list')
    else:
        form = MenuForm(instance=plat)
    
    return render(request, 'menu/menu_form.html', {'form': form, 'form_title': form_title})



def menu_delete(request, id):
    menu = get_object_or_404(Menu, id=id)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    #return render(request, 'menu_confirm_delete.html', {'menu': menu})
