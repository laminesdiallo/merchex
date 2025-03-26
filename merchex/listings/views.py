from .forms import ContactUsForm
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
def band_list(request):
    bands = Band.objects.all()
    return render(
        request,
        'listings/band_list.html',
        {'bands': bands},
    )


def about(request):
    return HttpResponse('<h1>A Propos</h1><p>Nous adorons merch !</p>')

def listings(request):

    return HttpResponse('<h1>A Propos</h1><p>Voici la liste !</p>')

def band_detail(request, id):
   return render(request,
          'listings/band_detail.html',
         {'id': id})

def contact(request):
  form = ContactUsForm()
  return render(request,
          'listings/contact.html',
          {'form': form})
