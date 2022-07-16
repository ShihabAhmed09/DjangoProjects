from django.shortcuts import render, redirect
from .models import Category, Photo


def gallery(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery/gallery.html', context)


def add_photo(request):
    categories = Category.objects.all()
    if request.method == "POST":
        data = request.POST  # grabs all the data as dictionary
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
            # get_or_create() look for the category in database, if not found then create a new or get the existing one
        else:
            category = None

        photo = Photo.objects.create(category=category, description=data['description'], image=image)

        return redirect('gallery:gallery')

    context = {'categories': categories}
    return render(request, 'gallery/add_photo.html', context)


def photo_view(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo}
    return render(request, 'gallery/photo_view.html', context)
