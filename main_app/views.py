from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView, DeleteView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(event=self.object)
        context['user'] = self.request.user
        return context


class ReviewList(ListView):
    model = Review
    context_object_name = 'review'
    template_name = 'events/details.html'
    # template_name = 'events/review_list.html'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        event = Events.objects.get(id=self.kwargs['pk'])
        return Review.objects.filter(event=event)

class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'comment', 'date']
    pk_url_kwarg = 'event_id'

    def form_valid(self, form):
        form.instance.event = Events.objects.get(id=self.kwargs['event_id'])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.object.event.pk})

class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['user', 'rating', 'comment', 'date']
    template_name = 'main_app/review_form.html'
    pk_url_kwarg = 'review_id'
    
    def get_success_url(self):
        event = self.object.event
        return reverse('details', kwargs={'pk': event.pk})

class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'events/review_confirm_delete.html'
    pk_url_kwarg = 'review_id'
    
    def get_success_url(self):
        event = self.object.event
        return reverse('details', kwargs={'pk': event.pk})

@login_required
def my_events(request):
    try:
        events = request.user.profile.events.all()
        return render(request, 'my_events.html', {'events': events})
    except:
        return render(request, 'my_events.html', {'events': None})
      
class MyEventsDelete(LoginRequiredMixin, DeleteView):
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