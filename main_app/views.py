from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Events, Review

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
    
class EventDetailsView(DetailView):
    model = Events
    template_name = 'events/details.html'
    context_object_name = 'event'
    pk_url_kwarg = 'pk'
    
class ReviewList(ListView):
    model = Review
    context_object_name = 'review'
    template_name = 'events/review_list.html'
    pk_url_kwarg = 'pk'
    
    def get_queryset(self):
        event = Events.objects.get(id=self.kwargs['pk'])
        return Review.objects.filter(event=event)
    
class ReviewCreate(CreateView):
    model = Review
    fields = '__all__'
    pk_url_kwarg = 'review_id'
    
    def form_valid(self, form):
        form.instance.event = Events.objects.get(id=self.kwargs['pk'])
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdate(UpdateView):
    model = Review
    fields = '__all__'
    template_name = 'events/review_form.html'
    pk_url_kwarg = 'review_id'

class ReviewDelete(DeleteView):
    model = Review
    template_name = 'events/review_confirm_delete.html'
    fields = 'review_id'
    pk_url_kwarg = 'review_id'

@login_required
def my_events(request):
    events = request.user.profile.events.all()
    return render(request, 'my_events.html', {'events': events})

class MyEventsDelete(DeleteView):
    model = Events
    template_name = 'my_events_confirm_delete.html'
    pk_url_kwarg = 'event_id'
    success_url = reverse_lazy('my_events')

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
