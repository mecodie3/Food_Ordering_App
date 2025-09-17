from django.urls import path
from . import views

#string empty for homepage
urlpatterns = [
    path('',views.MenuList.as_view(),name='home')
]
