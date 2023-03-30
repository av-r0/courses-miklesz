from django.http import HttpResponse
from django.shortcuts import render
from movies.models import *
from datetime import datetime  # NOWE


# # Create your views here.
# def hello_world(request):
# #     return HttpResponse("Witaj świecie!")
#     return render(request, template_name="hello.html")  # NOWE

# Create your views here.
def hello_world(request):
    our_context = {"time": datetime.now()}  # NOWE
    return render(request, template_name="hello.html", context=our_context)  # NOWE

def list_movies(request):
    movies = Movie.objects.all()
    return render(request, template_name="movie_list.html", context={"movies": movies})
