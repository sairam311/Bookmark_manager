from django.shortcuts import render, redirect
from .models import User

def urls(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        url = data.get('url')
        User.objects.create(name=name, url=url)
        return redirect('/')

    queryset = User.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    context = {'urls': queryset}
    return render(request, 'urls.html', context)

def delete_url(request, id):
    url = User.objects.get(id=id)
    url.delete()
    return redirect('/')

def update_url(request, id):
    url = User.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        url_value = data.get('url')  # Use a different variable name to avoid shadowing

        url.name = name
        url.url = url_value
        url.save()
        return redirect('/')

    context = {'url': url}
    return render(request, 'update_url.html', context)

def favorite_url(request, id):
    url = User.objects.get(id=id)
    url.favorite = not url.favorite
    url.save()
    return redirect('/')