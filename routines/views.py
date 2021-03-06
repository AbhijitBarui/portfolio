from django.shortcuts import redirect, render
from .models import Routine
from datetime import datetime
from .forms import RoutineForm
weekday = datetime.today().strftime('%A')


def routine(request):
    # routine = Routine.objects.all().filter(day=datetime.today().strftime('%A'))
    try:
        routine = Routine.objects.get(day=weekday)
    except:
        routine = Routine(day=weekday)
        routine.save()
    #routine = Routine.objects.all().filter(day=weekday)
    context = {
        'routine':routine,
    }
    return render(request, 'routines/routine.html', context)


def getroutine(request):
    form = RoutineForm
    context = {
        'form':form,
    }
    return render(request, 'routines/routineform.html', context)

def postroutine(request):
    routine = Routine.objects.get(day=weekday)
    form = RoutineForm(request.POST, instance=routine)
    if form.is_valid():
        form.save()
        return redirect('routine')