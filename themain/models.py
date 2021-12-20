from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Mavzu', max_length=100)
    matn = models.TextField('Maqola matni')
    muallif = models.CharField('Maqola muallifi', max_length=30)
    sana = models.DateField('Nashr sanasi')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'