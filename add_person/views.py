from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def results(request):
    if request.method == "POST":
        name = request.POST['name']
        location = request.POST['location']
        favorite = request.POST['favorite']
        comment = request.POST['comment']
        gender = request.POST['gender']
        request.session['name'] = name
        request.session['location'] = location
        request.session['favorite'] = favorite
        request.session['comment'] = comment
        request.session['gender'] = gender
    return redirect('/info')

def info(request):
    return render(request, 'post.html')

# Create your views here.
