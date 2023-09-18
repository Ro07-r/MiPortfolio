from django.db import models

class Formulario(models.Model):
    nombre = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    texto = models.TextField(max_length=200)

    def __str__(self):
        return(self.nombre, self.mail, self.texto)
