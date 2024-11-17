from django.contrib import admin
from esporteblog.models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'age', 'goals', 'assists')  #usado para listar os campos que vão aparecer no registro do jogador
    search_fields = ('name', 'team') #usado para escolher o que será pesquisado
admin.site.register(Player, PlayerAdmin) #usado para registrar no server. tem que os dois parâmetros
