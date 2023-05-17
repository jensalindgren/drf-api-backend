from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowerList.as_view()),
    path('followers/<int:pk>/', views.FollowerDetail.as_view()),
    path('followedevents/', views.FollowedEventsList.as_view()),
    path('followedevents/<int:pk>/', views.FollowerEventsDetail.as_view()),
]
