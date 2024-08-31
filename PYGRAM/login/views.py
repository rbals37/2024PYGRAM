from django.shortcuts import render

#main
def login(quest):
    return render(quest,'login.html')
