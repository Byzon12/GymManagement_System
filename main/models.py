from django.db import models
from django.utils.html import mark_safe
#rom .forms import EnquiryForm
from django.contrib.auth.models import User


# Banner model
class Banners(models.Model):
    alt_text = models.CharField(max_length=150)
    img = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))


# Services model
class Services(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to='services/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))


# Sites model
class Page(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    img=models.ImageField(upload_to='pages/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))
    
#fqa model
class Fqa(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
#query models
class Enquiry(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    send_date = models.DateTimeField(auto_now_add=True)
    send_location = models.CharField(max_length=150)
    
    def __str__(self):
        return self.full_name
    
    #Gallery model
class Gallery(models.Model):
    title = models.CharField(max_length=150)
    detail=models.TextField(max_length=500, null=True, blank=True)
    img = models.ImageField(upload_to='gallery/')
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))
    
    #GalleryImage model
class GalleryImage(models.Model):
    alt_text = models.CharField(max_length=15, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='gallery_image/')
    
    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))
    
    #subscription plan model
class Subplan(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    max_member=models.IntegerField(null=True, blank=True)
    price = models.CharField(max_length=150)
    highlight_status = models.BooleanField(default=False, null=True, blank=True)
 
    def __str__(self):
        return self.title
    
#subscription feature model
class Subfeature(models.Model):
    title = models.CharField(max_length=150)
    subplan = models.ManyToManyField(Subplan)
    #= models.CharField(max_length=150, null=True, blank=True)
    #subplan = models.ForeignKey(Subplan, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
#package discount model
class PlanDiscount(models.Model):
    subplan = models.ForeignKey(Subplan, on_delete=models.CASCADE, null=True, blank=True)
    total_month = models.IntegerField()
    total_discount = models.IntegerField()
    
    def __str__(self):
        return self.subplan.title
    
    #subcribers
class Subscribers(models.Model):
    User=models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    img=models.ImageField(upload_to='subs/', null=True, blank=True)
    
    def __str__(self):
        return self.full_name
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))
    
    #subcribeription(models)
class Subscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    plan=models.ForeignKey(Subplan, on_delete=models.CASCADE)
    start_date=models.DateTimeField(auto_now_add=True)
    price=models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username
    