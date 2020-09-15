from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
posts = [
    {
        'author': 'Mike B',
        'title': 'blog-post1',
        'content': '1st post content',
        'date_posted': '15 wrz 2020'
    },
    {
        'author': 'Mike C',
        'title': 'blog-post2',
        'content': '2st post content',
        'date_posted': '16 wrz 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
