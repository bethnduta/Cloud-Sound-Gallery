from django.shortcuts import render,redirect
from .models import Category, Photo
# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)

def viewPhoto(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo':photos})

def addPhoto(request):
    categories = Category.objects.all()
    
    if request.method== 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] !='none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] !='':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else: 
            category = None
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )      
        return redirect('gallery')     


    context = {'categories': categories}
    return render(request, 'add.html', context)

def search(request):
      if 'category' in request.GET and request.GET['category']:
        category = request.GET.get('category')
        photos = Photo.objects.filter(category__name__icontains=category)
        return render(request, 'search.html', {'photos':photos})