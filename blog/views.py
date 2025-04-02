from django.shortcuts import render, redirect
from .models import Blog
# Create your views here.

def blogs(request):
    blogs = Blog.objects.all()
    if blogs is not None:
        return render(request, 'blogs.html', {'blogs':blogs})
    else:
        print('Whoops! No blog found.')
    return True

def remove_blog(request, id):
    Blog.objects.get(id=id).delete()
    print('Blog removed')
    return redirect('blogs')

def blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'view_blog.html', {'blog':blog})

def update_blog(request):
    id = request.POST['id']
    comment = request.POST['comment']
    blog = Blog.objects.filter(id=id).exists()
    if blog is not None:
        Blog.objects.filter(id=id).update(comment=comment, like=True)
    else:
        print('Whoops! Blog not exists')
        return redirect("blog")
    return redirect('blogs')