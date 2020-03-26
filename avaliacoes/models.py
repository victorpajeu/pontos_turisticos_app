from django.db import models
from django.contrib.auth.models import User


class Avaliacoes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    aprovado = models.BooleanField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
