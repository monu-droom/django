from django.shortcuts import render, redirect
import random
# Create your views here.

def find_ball(request):
    win = 0
    balls = [0, 0, 1]
    random.shuffle(balls)
    if request.method == 'POST':
        location = request.POST['choice']
        pos = balls.index(1)
        if pos == int(location):
            win = 1
        return render(request, 'findball_result.html', {'win': win, 'pos': pos, 'pc': int(location)})
    else:
        return render(request, 'findball.html')