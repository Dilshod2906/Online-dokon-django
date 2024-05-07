from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Yaratildi'),
        (PAID, 'To\'langan'),
        (ON_WAY, 'Yo\'lda'),
        (DELIVERED, 'Yetkazildi')

    )
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return f"Order {self.id} | {self.first_name}, {self.last_name}"
