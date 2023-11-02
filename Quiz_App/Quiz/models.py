from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    op1 = models.CharField(max_length=150)
    op2 = models.CharField(max_length=150)
    op3 = models.CharField(max_length=150)
    op4 = models.CharField(max_length=150)
    ANSWER_CHOICES = [
        ('op1', 'Option 1'),
        ('op2', 'Option 2'),
        ('op3', 'Option 3'),
        ('op4', 'Option 4'),
    ]
    answer = models.CharField(max_length=3, choices=ANSWER_CHOICES)
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Question' 
        verbose_name_plural = 'Questions' 

    def save(self, *args, **kwargs):
        if not self.pub_date:
            self.pub_date = timezone.now()
        super(Question, self).save(*args, **kwargs)
