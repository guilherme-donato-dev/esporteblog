from django.shortcuts import render
from esporteblog.models import Player

# Create your views here.

def players_view(request):
        players = Player.objects.all()

        return render()
