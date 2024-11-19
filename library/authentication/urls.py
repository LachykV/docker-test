from django.urls import path, include
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('myroom/', views.myroom, name="myroom"),
    path('logout/', views.logout_view),
    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls'))
]