from django.db import models


class RegisteroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text="Motivo hora extra")

    def __str__(self):
        return self.motivo
