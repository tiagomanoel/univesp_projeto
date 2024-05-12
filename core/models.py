from django.db import models

class law(models.Model):
    id_law = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    ano = models.ImageField()
    situacao = models.TextField()
    title = models.TextField()
    arq = models.FileField(upload_to="pdf")
    texto = models.TextField()

def __str__(self) -> str:
    return self.title
def __str__(self):
    return self.texto  
