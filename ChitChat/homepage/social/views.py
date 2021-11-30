from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Post, Comment, UserProfile
from .forms import CommentForm, PostForm
from django.views.generic.edit import UpdateView, DeleteView


class PostListView(LoginRequiredMixin,View):
# sets the post to have all form functions from models.py
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on') #uses created on variable to order posts from newest to oldest. 
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'social/post_list.html', context)

#when user hits submit button on post

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST, request.FILES) #request.FILES is for sending a request for the image !!!very important
        

#saves post on to page
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'social/post_list.html', context)
#allows you to click on the post which sends you to the official page of the post.
class PostDetailView(LoginRequiredMixin, View):
        def get(self, request, pk, *args, **kwargs):
            post = Post.objects.get(pk=pk)
            form = CommentForm()
            comments = Comment.objects.filter(post=post).order_by('-created_on')
            context = {
                'post': post,
                'form': form,
                'comments': comments
            }

            return render(request, 'social/post_detail.html', context)
        def post(self, request, pk, *args, **kwargs):
            post = Post.objects.get(pk=pk)
            form = CommentForm(request.POST)

            if form.is_valid():
                new_comment = form.save(commit = False)
                new_comment.author = request.user
                new_comment.post = post
                new_comment.save()

            comments = Comment.objects.filter(post=post).order_by('-created_on')


            context = {
                'post': post,
                'form': form,
                'comments': comments
            }

            return render(request, 'social/post_detail.html', context)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Post
        fields = ['body', 'art']
        template_name = 'social/post_edit.html'

        def get_success_url(self):
            pk = self.kwargs['pk']
            return reverse_lazy('post_detail', kwargs = {'pk':pk})
#test is a user can only access a post that they made.
        def test_func(self):
            post = self.get_object()
            return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
        model = Post
        template_name = 'social/post_delete.html'
        success_url = reverse_lazy('post_list')

        def test_func(self):
            post = self.get_object()
            return self.request.user == post.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
            pk = self.kwargs['post_pk']
            return reverse_lazy('post_detail', kwargs = {'pk':pk})

    def test_func(self):
            post = self.get_object()
            return self.request.user == post.author

class ProfileView(View): #pk (primary key) differentiates profiles
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('created_on')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts
        }

        return render(request, 'social/profile.html', context)
