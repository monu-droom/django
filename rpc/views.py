from django.shortcuts import render
import random
# Create your views here.
def rpc(request):
    if request.method == 'POST':
        pc = request.POST['choice']
        rpc_list = ['rock', 'paper', 'scissor']
        cc = random.choice(rpc_list)
        win = ''

        if pc == cc:
            win = 'Draw'
        elif pc == 'rock' and cc == 'paper':
            win = 'cc'
        elif pc == 'paper' and cc == 'scissor':
            win = 'cc'
        elif pc == 'scissor' and cc == 'rock':
            win = 'cc'
        else:
            win = 'pc'
        choices = [pc, cc]
        return render(request, 'rpc_win.html', {'win': win, 'pc': pc, 'cc': cc})
    else:
        return render(request, 'rpc.html')