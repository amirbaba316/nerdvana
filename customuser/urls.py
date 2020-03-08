from django.urls import path
from .views import CreateUserView,LoginView,LogoutView,HomePageView

urlpatterns=[
    path('homepage/',HomePageView.as_view(),name="homepage"),
    path('create/',CreateUserView.as_view(),name='create'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]