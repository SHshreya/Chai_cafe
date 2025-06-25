from django.db import models  # type: ignore
from django.utils import timezone # type: ignore
from django.contrib.auth.models import User  # type: ignore
# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','MASALA'),
        ('CL','COLDICE'),
        ('GR','GINGER'),
        ('PL','PLAIN'),
        ('EL','ELAICHI'),
        ('KI','KIWI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE) 
    chai_description = models.TextField(default='')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    availability = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Chai Varieties"
    def __str__(self):
      return self.name
    

#one to many
class ChaiReview(models.Model):
   chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
   user = models.ForeignKey(User, on_delete= models.CASCADE)
   rating = models.IntegerField()
   comment = models.TextField()
   date_added = models.DateTimeField(default = timezone.now)


   def __str__(self):
      return f'{self.user.username} review for {self.chai.name}'
      

#many to many
class Store(models.Model):
   name = models.CharField(max_length=100)
   location = models.CharField(max_length =100)
   chai_varieties = models.ManyToManyField(ChaiVariety,related_name='stores')


   def __str__(self):
      return self.name  
   


#one to one 
class ChaiCertificate(models.Model):
   chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
   certificate_number = models.CharField(max_length=100)
   issued_date = models.DateTimeField(default = timezone.now)
   valid_until = models.DateTimeField()


   def __str__(self):
      return f'certificate for {self.name.chai}'
   
       
