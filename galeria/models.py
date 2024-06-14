from datetime import datetime
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
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank = True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateField(default=datetime.now, blank = False)

def __str__(self):
    return self.nome