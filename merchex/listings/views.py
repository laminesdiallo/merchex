from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return render(
        request,
        'listings/hello.html',
        {'bands': bands}
    )

def about(request):
    return HttpResponse('<h1>A Propos</h1><p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Contact</h1><p>Envoyez-nous un email à contact@mercher.com</>')

def listings(request):

    return HttpResponse('<h1>A Propos</h1><p>Voici la liste !</p>')
