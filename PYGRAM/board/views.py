from django.shortcuts import render

# Create your views here.
def board(quest):
    return render(quest,'board.html')