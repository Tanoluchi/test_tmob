from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

class Redirect(models.Model):
    key = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Redirect'
        verbose_name_plural = 'Redirects'
        ordering = ['-created_at']

@receiver(post_save, sender=Redirect)
def save_cache(sender, instance, **kwargs):    
    """
    Cada vez que se realiza un cambio sobre un objeto de la clase Redirect
    se buscaran los todos los objetos que contengan el campo active=True
    y se guardara en la cache
    """
    redirects = Redirect.objects.filter(active=True)
    for redirect in redirects:
        cache.set(redirect.key, redirect.url)