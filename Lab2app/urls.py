from readline import append_history_file
from django.urls import path
from Lab2app import views
app_name = 'rango'
urlpatterns= [
    path('',views.index,name= 'index'),
]