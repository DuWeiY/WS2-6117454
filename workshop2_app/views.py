from django.shortcuts import render
from .models import movie
from django.http import HttpResponseRedirect, HttpResponse
import json

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def movie_list(request):
    #qs = PlayVideo.objects.all()
    list = [{'movie id': x.movie_id, 'title': x.movie_name, 'year': str(x.year),'genre': x.genre,
         }
            for x in movie.objects.order_by('movie_id')]
    #qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')


def movie_detail(request):
    movie_name = request.GET.get('movie_name')
    this_movie = movie()

    for x in movie.objects.filter(movie_name=movie_name):
        this_movie = x

    list = [{
        'movie_id': this_movie.movie_id,
        'movie_name': this_movie.movie_name,
        'year': this_movie.year,
        'genre': this_movie.genre,
    }]
    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')