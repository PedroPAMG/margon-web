from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 30, verbose_name='Titulo')
    description = RichTextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to = "projects")
    link = models.URLField(verbose_name='Link', null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de Crecion')
    updated = models.DateTimeField(auto_now = True, verbose_name='Fecha de Actualizacion')

    class Meta:
        verbose_name = 'Proyectos'
        verbose_name_plural = 'Proyectos'
        ordering = ["-created"]
    
    def __str__(self):
        return self.title