from django.contrib import admin

# Register your models here.
from .models import Categoria, Mensagem, Tag

@admin.register(Categoria)                                       # ← novo
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

@admin.register(Tag)                                            # ← novo
class TagAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "criada_em")
    list_filter = ("categoria", "tags")
    search_fields = ("titulo", "conteudo")
    filter_horizontal = ("tags",)
