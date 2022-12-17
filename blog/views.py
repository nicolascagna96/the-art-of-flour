from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, TemplateView, View
from .forms import CommentForm
from .forms import SubmitForm
from .forms import ContactForm
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .models import Comment
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

# CRUD


class CreatePostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Post
    template_name = "submit.html"
    fields = ['title', 'slug', 'content', 'featured_image']
    success_url = reverse_lazy('home')
    success_message = ("New post has been created - Waiting for approval")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(
    UserPassesTestMixin,
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    """ If user is logged can update a post """

    model = Post
    template_name = "submit.html"
    fields = ['title', 'slug', 'content', 'featured_image']
    success_url = reverse_lazy('home')
    success_message = ("Your Post has been updated")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView(
    UserPassesTestMixin,
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView
):
    """ If user is logged can delete a his post """

    model = Post
    template_name = "delete_post.html"
    success_message = ("Your Post has been deleted")
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePostView, self).delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Class used in the 'I think therefore I blog' walkthrough


class PostList(generic.ListView):

  
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

# Class used in the 'I think therefore I blog' walkthrough


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
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
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
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
                "comment_form": comment_form,
                "liked": liked
            },
        )

# Class used in the 'I think therefore I blog' walkthrough


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Contact database form


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


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'comment-delete.html'
    success_url = reverse_lazy('home')
