from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Contact, PostComment
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm


# def home(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'blog/post_list.html', context)


class PostListView(ListView):  # used as home page
    model = Post
    template_name = 'blog/home.html'  # original rule for template: <app>/<model>_<viewtype>.html (blog/post_list.html)
    context_object_name = 'posts'
    ordering = ['-publish_date']  # ordering from new to old
    paginate_by = 5


class UserPostListView(ListView):  # specific users post view page
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):  # get user associated with the username from url
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-publish_date')


class PostDetailView(DetailView):  # for blog post details view
    model = Post

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(slug=self.kwargs.get('slug')).first()

        comments = PostComment.objects.filter(post=post, parent=None)  # filtering actual comments
        replies = PostComment.objects.filter(post=post).exclude(parent=None)  # filtering replies

        reply_dict = {}
        for reply in replies:
            if reply.parent.serial_no not in reply_dict.keys():  # checking if reply parent is in dictionary
                reply_dict[reply.parent.serial_no] = [reply]  # appending parent if not present
            else:
                reply_dict[reply.parent.serial_no].append(reply)  # appending reply to existing parent

        # print(request.user)  # checking AnonymousUser or authenticated user
        context = {'object': post, 'comments': comments, 'reply_dict': reply_dict}
        if context['object'] is None:
            return HttpResponse("404 - Not Found")

        return render(request, 'blog/post_detail.html', context)


def post_comment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        post_id = request.POST.get('post_id')
        post = Post.objects.get(post_id=post_id)
        parent_serial_no = request.POST.get('parent_serial_no')

        if len(comment) == 0:
            return redirect(f"/post/{post.post_id}")

        if parent_serial_no == "":
            comment = PostComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Comment posted successfully")
        else:
            parent = PostComment.objects.get(serial_no=parent_serial_no)
            comment = PostComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Reply posted successfully")

        return redirect(f"/post/{post.slug}")
    else:
        return HttpResponse("404 - Not Found")


class PostCreateView(LoginRequiredMixin, CreateView):  # for creating new blog post
    # LoginRequiredMixin ensures to login before posting
    model = Post
    fields = ['title', 'content']
    extra_context = {'title': 'Create Post'}

    # template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  # running form_valid() on parent class after author is set


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # for updating post
    # UserPassesTestMixin restricts user from updating others posts.
    model = Post
    fields = ['title', 'content']
    extra_context = {'title': 'Update Your Post'}

    # template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  # running form_valid() on parent class after author is set

    def test_func(self):  # LoginRequiredMixin will run this to see if user passes certain test conditions
        post = self.get_object()  # get the post trying to update
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # for deleting post
    model = Post
    success_url = '/'

    # def get_success_url(self):
    #     return reverse('/')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SearchPostListView(ListView):  # used as home page
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')

        if query:
            posts = Post.objects.filter(Q(title__icontains=query) |
                                        Q(author__username__icontains=query)).order_by('-publish_date')
        else:
            posts = Post.objects.all().order_by('-publish_date')  # Post.objects.none()

        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj, 'query': query, 'query_length': len(query), 'title': 'Search Results'}
        template_name = 'blog/search_posts.html'

        """
        try:
            posts = paginator.page(page)
        except PageNotAnInteger :
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        """

        return render(request, template_name, context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, label_suffix='')
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for contacting us. Our admin panel will contact you shortly.")
            return redirect('blog_contact')
    else:
        form = ContactForm(label_suffix='')
    return render(request, 'blog/contact.html', {'title': 'Contact', 'form': form})
