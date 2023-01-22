from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('events/', views.index, name='index'),
    path('my-events', views.my_events, name='my_events'),
    path('all-events/<int:event_id>/', views.event_details, name='details')
]
