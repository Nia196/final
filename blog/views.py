from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import UpdateView
from blog.models import Post
from blog.forms import PostForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(TemplateView):
    template_name = 'home.html'

def restricted_view(request):
    return HttpResponse("you can not access to this page")

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

