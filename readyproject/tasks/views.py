from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, TaskSerializer

# this project is done in different apps it is my first project with different app
# i have created a task management app with api and admin dashboard

@api_view(['GET', 'POST'])
def TaskListAPI(request):
    if request.method == 'GET':
        tasks=  Task.objects.all()
        serializer= TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data= request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def CategoryListAPI(request):
    if request.method == 'GET':

        categories = Category.objects.all()
        catdata = CategorySerializer(categories, many=True)
        return Response(catdata.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def totaltasks(request):
    total = Task.objects.count()
    return Response({'total_tasks': total})

@api_view(['GET'])
def totalcategories(request):
    total = Category.objects.count()
    return Response({'total_categories': total})

@api_view(['GET', 'POST'])
def delete_all_tasks(request, id):
    dele = get_object_or_404(Task, id=id)
    dele.delete()
    return redirect('taskdetails')







# Create your views here.
@login_required(login_url='login')
def taskopen(request):
    return render(request, 'task.html')

def op(request):
    return render(request, 'task/taske.html')

@login_required(login_url='login')
def create_task(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title= request.POST.get('title')
        category_id = request.POST.get('category')
        owner = request.user
        category = Category.objects.get(id=category_id) if category_id else None
        Task.objects.create(title=title, owner=owner, category=category)
        return redirect('taskdetails')
    return render(request, 'task/tasks.html', {'categories': categories})

@login_required(login_url='login')
def taskdetails(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'task/taskdetails.html', {'tasks': tasks})


@login_required(login_url='login')
def taskdelete(request, id):
    task = Task.objects.get(id= id)
    task.delete()
    return redirect('taskdetails')


@login_required(login_url='login')
def taskupdate(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        task.title = title
        task.save()
        return redirect('taskdetails')
    return render(request, 'task/taskupdate.html', {'task': task})



@login_required(login_url='login')
def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
    return render(request, 'task/create_category.html')



def admindashboard(request):
    total = Task.objects.count()
    total_categories = Category.objects.count()
    recent_tasks = Task.objects.all().order_by('-id')[:5] 
    
    context = {
        'total': total, 
        'total_categories': total_categories,
        'recent_tasks': recent_tasks,
        'admin_name': request.user.username,
    }
    return render(request, 'task/admin.html', context)