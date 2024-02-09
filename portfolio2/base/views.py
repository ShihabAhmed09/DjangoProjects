from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q

from .models import Skill, Contact, Certificate, Project, Tag, Post, PostComment
from .forms import ContactForm
from .filters import PostFilter
from .decorators import *


def base_home(request):
    message = Contact.objects.filter(is_read=False).count()
    request.session['messages'] = message
    context = {}
    return render(request, 'base/base_home.html', context)


def about(request):
    skills = Skill.objects.all()
    certificates = Certificate.objects.all()
    context = {'skills': skills, 'certificates': certificates}
    return render(request, 'base/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f"Thanks for contacting. I'll try to contact you back as soon as possible.")
            return redirect('contact')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'base/contact.html', context)


def projects(request):
    all_project = Project.objects.filter(active=True)
    tags = Tag.objects.all()

    category = request.GET.get('q')

    if category is None:
        all_project = all_project
    else:
        category = category.strip()
        all_project = all_project.filter(Q(tags__name__icontains=category))

    context = {'all_project': all_project, 'tags': tags, 'category': category}
    return render(request, 'base/projects.html', context)


def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)

    context = {'project': project}

    if project.slug == 'django-blog':
        return render(request, 'base/project_blog.html', context)
    elif project.slug == 'a-simple-todo-app':
        return render(request, 'base/project_todo_app.html', context)
    elif project.slug == 'django-crud-operation':
        return render(request, 'base/project_crud_operation.html', context)


def blog_home(request):
    posts = Post.objects.filter(active=True)

    my_filter = PostFilter(request.GET, queryset=posts)
    posts = my_filter.qs

    page = request.GET.get('page')

    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts, 'my_filter': my_filter}
    return render(request, 'base/blog_home.html', context)


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')

        PostComment.objects.create(author=name, post=post, comment=comment)
        messages.success(request, "You're comment was successfully posted!")

        return redirect('post-details', slug=post.slug)

    # posts = Post.objects.filter(active=True, featured=True).exclude(title=post.title)[:3]
    posts = Post.objects.filter(active=True, featured=True)[:3]

    context = {'post': post, 'posts': posts}

    if post.slug == 'to-do-app-django':
        return render(request, 'base/post_todo_app.html', context)
    elif post.slug == 'best-videos-for-learning-python':
        return render(request, 'base/post_learning_python.html', context)
    elif post.slug == 'the-best-programming-podcasts':
        return render(request, 'base/post_programming_podcasts.html', context)
