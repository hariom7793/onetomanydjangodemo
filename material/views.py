from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import Material, Subcategory, Category


def index(request):
    all_materials = Material.objects.all()
    context = {
        'all_materials': all_materials
    }
    return render(request, 'material/index.html', context)


def detail(request, material_id):
    try:
        category = Category.objects.get(subcategory__material__id=material_id)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    return render(request, 'material/detail.html', {'category': category})


def new(request):
    if request.method == 'POST':
        if request.POST:
            material = Material()
            material.name = request.POST['name']
            material.description = request.POST['description']
            material.quantity = request.POST['quantity']
            material.subcategory = Subcategory.objects.get(name=request.POST['subcategory'])
            material.save()
        return redirect('index')
    subcategories = Subcategory.objects.all()
    return render(request, 'material/new.html', {'subcategories': subcategories})





















