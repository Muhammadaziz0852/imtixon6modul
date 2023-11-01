from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Todos(models.Model):
    text = models.TextField()
    expires_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Servic'
        verbose_name_plural = 'Servics'

    def __str__(self):
        return f'{self.text} from {self.owner}'
