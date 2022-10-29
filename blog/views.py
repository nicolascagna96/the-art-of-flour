from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, TemplateView, View
from .forms import CommentForm
from .forms import SubmitForm
from .forms import ContactForm
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .models import Recipes


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


def about_page(request):

    """
    Viewing the about page.
    """
    return render(request, 'about.html,', {})


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def submit(request):

    if not request.user.is_authenticated:
        messages.error(request, "You must login before you can submit")
        return redirect("/account/login/")
        form = None

    if request.method == "POST":
        form = SubmitForm(request.POST, request.FILES)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your recipe has been sent successfully!')
            return HttpResponseRedirect('/')
    else:
        form = SubmitForm()
        return render(
            request, 'submit.html', {'form': form})


def add_contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully!')
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
        form = ContactForm()
        return render(
            request, 'add_contact.html', {'form': form, 'submitted': submitted})
