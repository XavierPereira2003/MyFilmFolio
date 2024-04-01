from django.shortcuts import render,get_object_or_404
from . import models

# Create your views here.
def actor_list(request):
    actors = models.Cast.objects.all()
    return render(request, 'cast/actor_list.html', {'actors': actors})

def view_actor(request,actor_slug):
    actore_details=get_object_or_404(models.Cast,slug=actor_slug)
    return render(request,'cast/view_actor.html',{'actore_details':actore_details})