from django.db import models

# Create your models here.

JoP_Type = (

    ('full time' , 'full time'),
    ('part time' , 'part time'),

)
    

class job(models.Model): #table
    title = models.CharField( max_length=100) #column
    jop_type = models.CharField(max_length=15, choices=JoP_Type)
    discrations = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE)
    


    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
            
        
