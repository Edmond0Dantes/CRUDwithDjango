from django.db import models

# Create your models here.
class User(models.Model):

    name=models.CharField(max_length=150)

    phone=models.CharField(max_length=20)

    email=models.EmailField()

    address=models.TextField()


    def __str__(self):

        return self.name



class Order(models.Model):

    datetime=models.DateTimeField()

    purchase=models.CharField(max_length=150)

    purchase_id=models.IntegerField(primary_key=True)

    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):

        return str(self.purchase_id)