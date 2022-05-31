from django.shortcuts import render

# Create your views here.

def financing_choices(request):
    return render( request , 'calc/financing_choices.html' , {} )