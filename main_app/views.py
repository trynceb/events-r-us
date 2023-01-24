from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .models import Events

class HomeView(ListView):
    model = Events
    template_name = 'home.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return Events.objects.all()[:3]

class IndexView(ListView):
    model = Events
    template_name = 'events/index.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return Events.objects.all()
      
    def save_event(self, request):
        event = redirect('index')
        request.user.profile.events.add(event)
        return redirect('my_events')

class MyEventsView(LoginRequiredMixin, TemplateView):
    model = Events
    template_name = 'my_events.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return self.request.user.profile.events.all()
    

class EventDetailsView(DetailView):
    model = Events
    template_name = 'events/details.html'
    context_object_name = 'event'
    pk_url_kwarg = 'event_id'
    
class ReviewCreate(CreateView):
    model = Reviews
    template_name = 'events/details.html'
    context_object_name = 'review'
    pk_url_kwarg = 'review_id'
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, error_message='Invalid sign up - try again'))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


# def signup(request):
#   error_message = ''
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return redirect('index')
#     else:
#       error_message = 'Invalid sign up - try again'
#   form = UserCreationForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/signup.html', context)

  
# @login_required
def test(request):
    pass

class TestClass(LoginRequiredMixin,):
    pass
