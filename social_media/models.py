from django.db import models

# Create your models here.
class Social_Media(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titulo")
    url = models.URLField(verbose_name='Link', max_length=200, null=True, blank=True)
    icon = models.ImageField(verbose_name='Icono', upload_to = "iconos")
    created = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de Crecion')
    updated = models.DateTimeField(auto_now = True, verbose_name='Fecha de Actualizacion')

    class Meta:
        verbose_name = 'Redes Sociales'
        ordering = ['name',]
    
    def __str__(self):
        return self.name

