from django.urls import path
from events import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('events/<int:pk>/delete/', views.EventDelete.as_view()),
    path('events/<int:pk>/update/', views.EventUpdate.as_view()),
]
