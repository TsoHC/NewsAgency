from django.urls import path
from .views import LoginView, LogoutView, StoryView, DeleteStoryView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('stories/', StoryView.as_view(), name='stories'),
    path('stories/<int:key>/', DeleteStoryView.as_view(), name='delete_story'),
]