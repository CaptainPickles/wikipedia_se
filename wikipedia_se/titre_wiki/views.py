from django.shortcuts import render
from django.template.loader import render_to_string
import wikipedia
# Create your views here.

def index(request):
    ny = wikipedia.page("New York City")
    context = {
        "titre" : ny.title,
        "content" : ny.content
    }
    
    return render(request ,'home.html' , context)