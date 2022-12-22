from django.shortcuts import render
from .models import About
from home.models import About_home
from article.models import Article
from contact.models import ContactMe

# Create your views here.

def about_view(request):
    obj = About.objects.all()
    obj_about = About_home.objects.all()
    obj_index = Article.objects.all()[:2]
    obj_contactme = ContactMe.objects.all()

    ctx = {
        'abouts': obj,
        'about_homes': obj_about,
        'indexs': obj_index,
        'contactmes': obj_contactme
    }

    return render(request, 'about.html', ctx)
