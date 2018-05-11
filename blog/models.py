from django.db import models
from django.utils import timezone
class Post(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE) ##crea vinculo con otra tabla (modelo)
        title = models.CharField(max_length=200)#pone un limite en # de caracteres
        text = models.TextField() ## no tiene limite en los caracter, ideal para poner info
        created_date = models.DateTimeField( default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)
def publish(self): ##crea metodo para publicar  
         self.published_date = timezone.now()
         self.save()

def __str__(self): ##devuelve el titulo del blog
	 return self.title
