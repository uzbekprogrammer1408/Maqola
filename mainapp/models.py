from django.db import models

class Maqola(models.Model):
    muallif = models.TextField(verbose_name='muallif', max_length='50')
    mavzu = models.TextField(verbose_name='mavzu', max_length='255')
    matn = models.TextField(verbose_name='matn', max_length='255')
    

