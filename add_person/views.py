from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def results(request):
    if request.method == "POST":
        context = {
            "name": request.POST['name'],
            "location": request.POST['location'],
            "favorite": request.POST['favorite'],
            "comment": request.POST['comment'],
            "gender": request.POST['gender'],
        }
        return render(request, 'post.html', context)
    return render(request, 'post.html')

# Create your views here.
