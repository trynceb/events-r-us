from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.HomeView.as_view(), name='home'),
    path('events/', views.IndexView.as_view(), name='index'),
    path('my-events/', views.MyEventsView.as_view(), name='my_events'),
    path('events/<int:pk>/', views.EventDetailsView.as_view(), name='details'),
    path('reviews/create/', views.ReviewCreate.as_view(), name='review_create')
]

