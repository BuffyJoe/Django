from django.urls import path

from blog_app.forms import postform
from . import views
urlpatterns = [
    path('home/', views.index, name='home'),
    path('post/<int:pk>/', views.postview, name='post'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('login/', views.Loginpage, name='Login'),
    path('logout/', views.logoutpage, name="log-out"),
    path('delete/<str:pk>/', views.deletepost, name='delete'),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>', views.Profile, name="profile"),
    path('post/', views.like_post, name='like_post'),
]