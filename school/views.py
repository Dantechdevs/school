from django.shortcuts import render

def index(request):
    return render(request, 'authentication/login.html')

def dashboard(request):
    return render(request, 'students/student-dashboard.html')
    



