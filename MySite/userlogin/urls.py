from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'userlogin'

urlpatterns = [
    url(r"Home/Sign-Up/$",views.signup,name='signup'),
]