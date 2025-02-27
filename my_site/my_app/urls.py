from django.urls import path
from . import views
from django.views.generic import RedirectView


app_name='my_app'

urlpatterns = [
    path('create/',views.CreateToDo.as_view(),name='create'),
    path('list/',views.ListToDo.as_view(),name='list'),
    path('detail/<int:pk>',views.DetailToDo.as_view(),name='detail'),
    path('update/<int:pk>',views.UpdateToDo.as_view(),name='update'),
    path('delete/<int:pk>',views.DeleteToDo.as_view(),name='delete'),  
    path('',RedirectView.as_view(url='list')) 
]