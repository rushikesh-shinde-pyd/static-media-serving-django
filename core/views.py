from django.shortcuts import render
from .forms import FishForm
from .models import Fish


def home(request):
    context = {}
    if request.method == 'POST':
        form = FishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    fishes = Fish.objects.all()[::-1]
    context['form'] = FishForm()
    context['fishes'] = fishes

    return render(request, 'core/index.html', context)