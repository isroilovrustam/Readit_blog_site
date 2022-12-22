from django.shortcuts import render, redirect
from .forms import ContactForm
from home.models import Contact_home
from article.models import Article
from .models import ContactMe

# Create your views here.

def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    obj_contact = Contact_home.objects.all()
    obj_contactme = ContactMe.objects.all()
    obj_article = Article.objects.all()[:2]
    ctx = {
        'form': form,
        'homes': obj_contact,
        'contactmes': obj_contactme,
        'indexs': obj_article,
    }

    return render(request, 'contact.html', ctx)
