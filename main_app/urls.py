from django.urls import path
from .views import HomeView, IndexView, MyEventsView, EventDetailsView, SignUpView

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', HomeView.as_view(), name='home'),
    path('events/', IndexView.as_view(), name='index'),
    path('my-events/', MyEventsView.as_view(), name='my_events'),
    path('events/<int:pk>/', EventDetailsView.as_view(), name='details')
]

