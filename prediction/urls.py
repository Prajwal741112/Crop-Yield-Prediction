from django.urls import path
from .views import (
    predict_view,
    login_view,
    register_view,
    logout_view,
)

urlpatterns = [
    path('', predict_view, name='predict'),

    path('login/', login_view, name='login'),

    path('register/', register_view, name='register'),

    path('logout/', logout_view, name='logout'),
]