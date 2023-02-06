from django.shortcuts import render

# Create your views here.

def manager(request):
    return render(request, 'manager/manager.html')
def rename_auto(request):
    return render(request, 'manager/rename_auto.html')
def rename_manual(request):
    return render(request, 'manager/rename_manual.html')
def new_direction(request):
    return render(request, 'manager/new_direction.html')
def move(request):
    return render(request, 'manager/move(.html')
def remove(request):
    return render(request, 'manager/remove.html')
def search(request):
    return render(request, 'manager/search.html')
