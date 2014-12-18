from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from django_ajax.decorators import ajax

from ipware.ip import get_ip

from poll.models import Vote

def index(request):
  return render(request, 'index.html', {
    'letters': settings.LETTER_LIST,
    'poll_active': True
  })

@ajax
def vote(request, letter):
  Vote.objects.create(choice = letter, ip = get_ip(request))
  return 1

def results(request):
  bar = max(settings.LETTER_LIST, key = lambda x: Vote.objects.count_choice(x[0]))
  max_value = Vote.objects.count_choice(bar[0])
  if max_value == 0:
    max_value = 1
  letters = [(x[0], x[1], Vote.objects.count_choice(x[0]), int(100.0 * Vote.objects.count_choice(x[0]) / max_value)) for x in settings.LETTER_LIST]
  letters = sorted(letters, key = lambda x: -x[2])

  return render(request, 'results.html', {
    'letters': letters,
    'results_active': True
  })
