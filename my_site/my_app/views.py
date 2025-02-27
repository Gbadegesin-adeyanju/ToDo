from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import ToDo
# Create your views here.

class CreateToDo(CreateView):
    model = ToDo
    fields = '__all__'
    success_url = reverse_lazy('my_app:list')

class ListToDo(ListView):
    model = ToDo
    queryset = ToDo.objects.order_by('created_time')
    context_object_name = 'todo_list'

class DetailToDo(DetailView):
    model = ToDo
    success_url = reverse_lazy('my_app:list')


class UpdateToDo(UpdateView):
    model = ToDo
    fields = '__all__'
    success_url = reverse_lazy('my_app:list')

class DeleteToDo(DeleteView):
    model = ToDo
    success_url = reverse_lazy('my_app:list')







