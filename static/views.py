from django.shortcuts import render

# Create your views here.
def alex(request):
    return render(request, 'jobs/alex.html')
