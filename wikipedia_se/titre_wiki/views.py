from django.shortcuts import render
from django.template.loader import render_to_string
import wikipedia
# Create your views here.

def index(request):
    wikipedia.set_lang("fr")
    titreArticle = []
    for i in range(1,100):
        titreArticle.append(wikipedia.random(pages=1))
    context = { "titre" : titreArticle}

    
    return render(request ,'home.html' , context)