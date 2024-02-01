from django.shortcuts import render

posts = [
    {
        'author': 'David',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'February 1, 2024'
    },
        {
        'author': 'David',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'February 2, 2024'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})