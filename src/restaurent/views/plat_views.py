from django.shortcuts import render, redirect, get_object_or_404
from restaurent.models.plat import Plat
from restaurent.forms.plat_form import PlatForm

def plat_list(request):
    plats = Plat.objects.all()
    plat_count = Plat.objects.count()

    context = {
            'plats': plats,
            'plat_count': plat_count,
            }
    
    return render(request, 'plat/plat.html', context)


def plat_form(request, id=None):
    if id:
        plat = get_object_or_404(Plat, id=id)
        form_title = "Modifier le plat"
    else:
        plat = None
        form_title = "Ajouter un plat"
    
    if request.method == 'POST':
        form = PlatForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('restaurent:plat_list')
    else:
        form = PlatForm(instance=plat)
    
    return render(request, 'plat/plat_form.html', {'form': form, 'form_title': form_title})


def plat_delete(request, id):
    plat = get_object_or_404(Plat, id=id)
    plat.delete()
    return redirect('restaurent:plat_list')

# def plat_delete(request, id):
#     plat = get_object_or_404(Plat, id=id)
#     if request.method == 'POST':
#         plat.delete()
#         return redirect('restaurent:plat_list')
    #return render(request, 'plat_confirm_delete.html', {'plat': plat})