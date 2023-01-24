from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.HomeView.as_view(), name='home'),
    path('events/', views.IndexView.as_view(), name='index'),
    path('my-events/', views.MyEventsView.as_view(), name='my_events'),
    path('events/<int:pk>/', views.EventDetailsView.as_view(), name='details'),
    path('events/<int:pk>/', views.ReviewList.as_view(), name='review_list'),
    path('events/<int:pk>/create/', views.ReviewCreate.as_view(), name='review_create'),
    path('events/<int:pk>/update/', views.ReviewUpdate.as_view(), name='review_update'),
    path('events/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review_delete')
]

