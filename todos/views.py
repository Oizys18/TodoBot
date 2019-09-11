from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Todo

def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request,'todos/index.html',context)

# def new(request):
#     print(request.method)
    

def create(request):
    # POST일 때 
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        Todo.objects.create(title=title, due_date=due_date)
        return redirect('todos:index')
    # GET 일 때 
    else:
        return render(request,'todos/create.html')
    

# def edit(request, pk):
    

def update(request, pk):
    # todo = get
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        todo.title = title
        todo.due_date = due_date
        todo.save()
        return redirect('todos:index')
    else:
        # print(request.method)
        context={
            'todo': todo,
        }
        return render(request,'todos/update.html', context)
    

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todos:index')