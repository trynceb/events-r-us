from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.HomeView.as_view(), name='home'),
    path('events/', views.IndexView.as_view(), name='index'),
    path('events/<int:pk>/delete', views.EventDetailsView.as_view(), name='details'),
    path('events/<int:pk>/reviews/', views.ReviewList.as_view(), name='review_list'),
    path('events/<int:event_id>/reviews/create/', views.ReviewCreate.as_view(), name='review_create'),
    path('reviews/<int:review_id>/update/', views.ReviewUpdate.as_view(), name="review_update"),
    path('events/reviews/<int:review_id>/delete/', views.ReviewDelete.as_view(), name='review_delete'),
    path('my-events/', views.my_events, name='my_events'),
    path('my-events/<int:event_id>/delete/', views.MyEventsDelete.as_view(), name='my_events_delete'),
]