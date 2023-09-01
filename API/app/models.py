from django.db import models
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome
class Applist(models.Model):
    tarefa = models.CharField(max_length = 20)
    choices_status = [
        ('1', 'Pronto'),
        ('2', 'Em andamento'),
        ('3', 'Pendente'),
    ]
    status = models.CharField(choices=choices_status, max_length=12)
    pessoa = models.ForeignKey(
        Pessoa,
        max_length=20,
        on_delete=models.CASCADE
    )
