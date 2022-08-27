from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll
# Create your views here.
def home(request):
    
    return render(request,'poll/home.html')

def allvote(request):
    context={}
    poll=Poll.objects.all()
    context={'polls':poll}
    return render(request,'poll/allvote.html',context)

def createpoll(request):
    context={}
    if request.method=='POST':
        form=CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
        context = {'form' : form}
    return render(request,'poll/createpoll.html',context)
  
def votepoll(request,poll_id):
    
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        print(request.POST['poll'])
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.op1_count += 1
        elif selected_option == 'option2':
            poll.op2_count += 1
        elif selected_option == 'option3':
            poll.op3_count += 1
        elif selected_option == 'option4':
            poll.op4_count+=1
        else:
            return HttpResponse(400, 'Invalid form option')
        return redirect('home')

        poll.save()
        return redirect('home')
    context = {
        'poll' : poll
    }
    return render(request,'poll/votepoll.html',context)
def result(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll' : poll
    }
   
    return render(request,'poll/result.html',context)\



      