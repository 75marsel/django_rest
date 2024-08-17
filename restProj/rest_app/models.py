from django.db import models
import uuid

class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    card_title = models.CharField(max_length=100)
    card_text = models.TextField(max_length=200)
    card_email = models.EmailField(max_length=100)
    card_link = models.URLField(max_length=200)
    card_footer = models.CharField(max_length=100)
    card_username = models.CharField(max_length=20)
    
    def __str__(self):
        return self.card_title