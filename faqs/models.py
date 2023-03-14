from django.db import models
from .choices import * 


class Language(models.Model):
    name = models.CharField(max_length=50, 
                            unique=True, 
                            verbose_name='Language Name',
                            choices=LANGUAGES, null=True, blank=True)
    code = models.CharField(max_length=10, 
                            unique=True, 
                            verbose_name='Language Code',
                            choices=LANGUAGES_CODES, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['-id']
    