from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime

# Create your models here.
class Category(models.Model):
          name=models.CharField(max_length=220)

          def  __str__(self):
            return self.name


class Sub_Category(models.Model):
          name =  models.CharField(max_length=220)
          category = models.ForeignKey(Category,on_delete=models.CASCADE)

          def  __str__(self):
            return self.name  
class Brand(models.Model):
          name = models.CharField(max_length=100)
          def  __str__(self):
               return self.name

class Products(models.Model):
         Category= models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default='')
         subcategory=models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=False,default='')
         brand=models.ForeignKey(Brand, on_delete=models.CASCADE,null=True)
         image= models.ImageField( upload_to='e_come')
         name= models.TextField(max_length=130)
         price=models.IntegerField()
         date=models.DateField( auto_now_add=True)
         
         def __str__(self):
             return self.name
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,label = 'Email',error_messages={'exists':'A user with this Email already exists.'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']   

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'          
    def save(self,commit=True):
      User=super(UserCreationForm,self).save(commit=False)
      User.email= self.cleaned_data['email']
      if commit:
        User.save()
      return User

    def clean_email(self):
      if User.objects.filter(email=self.cleaned_data['email']).exists():
        raise forms.ValidationError(self.fields['email'].error_messages['exists'])
      return self.cleaned_data['email']  
#contact_us
class  ContactUs(models.Model):
    name = models.CharField( max_length=50)
    email= models.EmailField( max_length=254)
    subject = models.CharField( max_length=50)
    message = models.TextField(max_length=500)
    def __str__(self):
             return self.email  

#order
class Order(models.Model):
     image = models.ImageField(upload_to='e_come')
     Product= models.CharField( max_length=500,default='')
     User= models.ForeignKey(User,on_delete=models.CASCADE)
     quantity = models.CharField( max_length=50)
     price = models.IntegerField()
     address = models.TextField(max_length=50)
     phone = models.CharField( max_length=10)
     pincode = models.CharField( max_length=6)
     date = models.DateField(default=datetime.datetime.today())
       
     def __str__(self):
             return self. Product