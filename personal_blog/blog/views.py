from django.shortcuts import render, get_object_or_404
from blog.models import Post
from .forms import ContactForm
def home(request):
    d = Post.objects.all()
    return render(request, 'blog/home.html', context = {'post':d})

def post_detail(request, id):
    post = get_object_or_404(Post, post_id = id)
    return render(request, 'blog/post_detail.html', {'p':post})

def contact(request):
    contact_form = ContactForm()
    return render(request, 'blog/contact.html', {'cf':contact_form})

def about(request):
    return render(request, 'blog/about.html')

