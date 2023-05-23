from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.BlogList.as_view()),
    path('<int:pk>/', views.BlogDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/create/', views.CreateUser.as_view()),
    path('users/current/', views.CurrentUserView.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('files/', views.FilePostViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

