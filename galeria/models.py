from django.db import models

class Fotografia(models.Model):

    categorias = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('PLANETA', 'Planeta'),
        ('GALÁXIA', 'Galáxia')
    ]

    nome = models.CharField(max_length=20, null = False, blank=False)
    legenda = models.CharField(max_length=150, null = False, blank=False)
    categoria = models.CharField(max_length=20, choices = categorias, default='')
    descricao= models.TextField(null = False, blank=False)
    foto = models.CharField(max_length=20, null = False, blank=False)

def __str__(self):
    return f'Fotografia [nome={self.nome}]'