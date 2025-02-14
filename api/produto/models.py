from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return self.categoria
    
    
class Produto(models.Model):
    produto = models.CharField('produto', max_length=100)
    unidade = models.CharField('unidade', max_length=3)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)
    preco = models.DecimalField('preço', max_digits=7, decimal_places=2)
    data = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
        
    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto


