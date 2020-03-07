from django.http import HttpResponse
from django.shortcuts import render




def index(request):

    context_dict = {'message': 'Message sent from the view'}

    return render(request, 'main/index-mainpage.html', context=context_dict)

def profile(request):
    
    return render(request, 'registration/profile.html')