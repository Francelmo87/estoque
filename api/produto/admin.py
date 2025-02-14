from django.contrib import admin

from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria')
    search_fields = ('categoria',)
   
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto','unidade','estoque','estoque_minimo','preco','data',)
    search_fields = ('produto',)
   