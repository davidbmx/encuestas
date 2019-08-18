from django.db import models

class AbstractModel(models.Model):
    """
    heredar a todos los modelos las fechas de creacion y actualizacion
    """

    created = models.DateField(
        'created at',
        auto_now_add=True,
        help_text='Fecha de creacion del modelo'
    )

    modified = models.DateField(
        'created at',
        auto_now=True,
        help_text='Fecha de actualizacion del modelo'
    )

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']

