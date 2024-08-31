from django.shortcuts import render

# Create your views here.
def signup_views(quest):
    return render(quest,'signup.html')