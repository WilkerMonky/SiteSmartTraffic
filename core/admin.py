from django.contrib import admin
from .models import Membro, Cargo, Registro, SugestoesModel


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo')


@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo')

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'etapa', 'objetivo', 'ativo')

@admin.register(SugestoesModel)
class SugestoesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ativo')