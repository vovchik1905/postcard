from enum import unique
from django.db import models


class EmailList(models.Model):
    email = models.EmailField(verbose_name = "Электронная почта",  unique=True)

    class Meta:
        ordering = ('email', )
        verbose_name = "Адрес email"
        verbose_name_plural = "Адреса email"
    
    def __str__(self):
        return self.email
