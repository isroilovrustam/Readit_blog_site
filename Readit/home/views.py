from django.shortcuts import render

from contact.models import ContactMe
from .models import Home
from article.models import Article
from django.core.paginator import Paginator
# Create your views here.


def home_view(request):
    obj = Home.objects.all()
    obj_article = Article.objects.all()[:8]
    p = Paginator(Article.objects.all(), 3)
    page = request.GET.get('page')
    obj_page = p.get_page(page)
    obj_index = Article.objects.all()[:2]
    obj_contactme = ContactMe.objects.all()

    ctx = {
        'homes': obj,
        'articles': obj_article,
        'pages': obj_page,
        'indexs': obj_index,
        'contactmes': obj_contactme
    }

    return render(request, 'home.html', ctx)