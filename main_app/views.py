from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Events

def home(request):
    events = Events.objects.all()
    return render(request, 'home.html', { 'events': events})

def index(request):
    events = Events.objects.all()
    return render(request, 'events/index.html', { 'events': events})

def my_events(request):
  return render(request, 'my_events.html')

def event_details(request, event_id):
  event= Events.objects.get(id=event_id)
  return render(request, 'events/details.html', {
    'events': event
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

  
@login_required
def test(request):
    pass

class TestClass(LoginRequiredMixin,):
    pass
