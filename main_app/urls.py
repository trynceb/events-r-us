from django.urls import path
from . import views
from .views import save_event

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.HomeView.as_view(), name='home'),
    path('events/', views.IndexView.as_view(), name='index'),
    path('events/<int:pk>/delete', views.EventDetailsView.as_view(), name='details'),
    path('events/<int:pk>/reviews/', views.ReviewList.as_view(), name='review_list'),
    path('events/<int:event_id>/reviews/create/', views.ReviewCreate.as_view(), name='review_create'),
    path('reviews/<int:review_id>/update/', views.ReviewUpdate.as_view(), name="review_update"),
    path('events/reviews/<int:review_id>/delete/', views.ReviewDelete.as_view(), name='review_delete'),
    path('my-events/', views.MyEventsView.as_view(), name='my_events'),
    path('events/<int:event_id>/add/', views.EventAddView.as_view(), name='event_add'),
    path('events/<int:event_id>/save', views.save_event, name='event_add'),
    path('my-events/<int:event_id>/delete/', views.MyEventsDelete.as_view(), name='my_events_delete'),
]