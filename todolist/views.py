from django.shortcuts import render,redirect


# Create your views here.

todolist = []
def index(request):
    if request.POST:
        new_task = request.POST['task']
        todolist.append(new_task.strip())
        return redirect('index')

    return render(request,'todolist/index.html',context={'task': todolist})




def about(request):
    return render(request,'todolist/aboutus.html')


def contact(request):
    return render(request,'todolist/contactus.html')
