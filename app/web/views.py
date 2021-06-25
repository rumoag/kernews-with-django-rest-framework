from django.shortcuts import render, redirect,reverse
from app.api.models import News
from app.web.forms import NewsForm
# Create your views here.

# Create your views here.
def home(request):
    return render(request,'pages/list.html', {})

def add_news(request):
    mi_form = NewsForm()
    #validar formulario
    if  request.method == 'POST':
        mi_form = NewsForm(request.POST)
        if mi_form.is_valid():
            #guardo
            mi_news_news = News()
            mi_news_news.title = request.POST['title']
            mi_news_news.url = request.POST['url']
            mi_news_news.save()
            #redirreciono a home
            return redirect(reverse('list'))
            #muestro errores

    return render(request,'pages/add-news.html', {
        'news_form': mi_form
    })