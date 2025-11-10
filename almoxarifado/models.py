from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=255) # max_lenght = varchar
    codigo = models.CharField(max_length=255, unique=True) # unique = único
    quantidade = models.IntegerField() #adicionar um campo de número interio
    categoria = models. CharField(max_length=255)
    data = models.DateField(auto_now_add=True) #auto_now_add=True cria a data AUTOMATICAMENTE

    def __str__(self):
        return self.nome