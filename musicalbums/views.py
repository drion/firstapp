from django.shortcuts import render
from django.http import HttpResponse

from musicalbums.models import Album



def index(request):
    return render(request, 'musicalbums/index.html', {'albums': Album.objects.all()})


def details(request, pk):
    return HttpResponse('<h1>Details for %(pk)s<h1>' % {'pk': pk})