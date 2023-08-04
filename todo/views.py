# from django.shortcuts import render
# from .models import TodoModel
# from .forms import TodoForm
# from django.views.generic import TemplateView,ListView
# from django.views.generic.edit import FormView,CreateView
# from django.urls import reverse_lazy
# # Create your views here.


# class home(TemplateView):
#     template_name = 'home.html'
   
    
# class todoFormView(CreateView):
#     model = TodoModel
#     template_name = 'todo.html'
#     form_class = TodoForm
#     success_url = reverse_lazy('todoform')
    

# class todoShowView(ListView):
#     model = TodoModel
#     template_name = 'todo.html'
#     context_object_name = 'data'



from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView,UpdateView,DeleteView
from .models import TodoModel
from .forms import TodoForm
from django.urls import reverse_lazy


class TodoFormShowView(FormView, ListView):
    model = TodoModel
    template_name = 'todo.html'
    form_class = TodoForm
    context_object_name = 'data'
    success_url = reverse_lazy('todoform')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = TodoModel.objects.all()
        return context
    

class todoUpdateView(UpdateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo.html'
    success_url = reverse_lazy('todoform')

class todoDeleteView(DeleteView):
    model = TodoModel
    template_name = 'delete_conformation.html'
    success_url = reverse_lazy('todoform')