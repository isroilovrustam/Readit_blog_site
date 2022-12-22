from django.shortcuts import render, redirect
from contact.models import ContactMe
from .models import Article, Category
from .forms import CommentForm
from .models import Comment
from home.models import Article_home, Single_home
from django.core.paginator import Paginator


# Create your views here.


def article_view(request):
    obj_home = Article_home.objects.all()
    obj = Article.objects.all()[:9]
    p = Paginator(Article.objects.all(), 3)
    page = request.GET.get('page')
    obj_page = p.get_page(page)
    obj_index = Article.objects.all()[:2]
    obj_contactme = ContactMe.objects.all()

    ctx = {
        'articles': obj,
        'pages': obj_page,
        'indexs': obj_index,
        'article_homes': obj_home,
        'contactmes': obj_contactme
    }

    return render(request, 'blog.html', ctx)


def single_view(request, pk):
    obj = Article.objects.get(id=pk)
    obj_index = Article.objects.all()[:2]
    obj_contactme = ContactMe.objects.all()
    obj_article = Article.objects.all()[:3]
    obj_single = Single_home.objects.all()
    obj_category = Category.objects.all()
    obj_comment = Comment.objects.all()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.article = obj
        com.save()
        return redirect('.')
    ctx = {
        'single': obj,
        'form': form,
        'homes': obj_single,
        'indexs': obj_index,
        'contactmes': obj_contactme,
        'comments': obj_comment,
        'single_articles': obj_article,
        'categorys': obj_category,
    }

    return render(request, 'blog-single.html', ctx)
