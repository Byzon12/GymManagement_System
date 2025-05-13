from django.db import models
from django.utils.html import mark_safe
#rom .forms import EnquiryForm
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models

# Banner model
class Banners(models.Model):
    alt_text = models.CharField(max_length=150)
    img = models.ImageField(upload_to='img/')
    
    class Meta:
        verbose_name_plural = 'Banners'
    
    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))


# Services model
class Services(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to='services/', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Services'
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))


# Sites model
class Page(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    img=models.ImageField(upload_to='pages/', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Pages'
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))
    
#fqa model
class Fqa(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    class Meta:
        verbose_name_plural = 'FQAs'
    
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
    
    class Meta:
        verbose_name_plural = 'Enquiries'
    
    def __str__(self):
        return self.full_name
    
    #Gallery model
class Gallery(models.Model):
    title = models.CharField(max_length=150)
    detail=models.TextField(max_length=500, null=True, blank=True)
    img = models.ImageField(upload_to='gallery/')
    
    class Meta:
        verbose_name_plural = 'Gallery'
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))
    
    #GalleryImage model
class GalleryImage(models.Model):
    alt_text = models.CharField(max_length=15, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='gallery_image/')
    
    class Meta:
        verbose_name_plural = 'Gallery Images'
    
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
    validity_days= models.IntegerField(null=True)
    
    class Meta:
        verbose_name_plural = 'Subscription Plans'
 
    def __str__(self):
        return self.title
    
#subscription feature model
class Subfeature(models.Model):
    title = models.CharField(max_length=150)
    subplan = models.ManyToManyField(Subplan)
    
    class Meta:
        verbose_name_plural = 'Subscription Features'
    #= models.CharField(max_length=150, null=True, blank=True)
    #subplan = models.ForeignKey(Subplan, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
#package discount model
class PlanDiscount(models.Model):
    subplan = models.ForeignKey(Subplan, on_delete=models.CASCADE, null=True, blank=True)
    total_month = models.IntegerField()
    total_discount = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Package Discounts'
    
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
    
    class Meta:
        verbose_name_plural = 'Subscribers'
    
    def __str__(self):
        return self.full_name
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Subscribers.objects.create(User=instance)
    
    
    #subcribeription(models)
class Subscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    plan=models.ForeignKey(Subplan, on_delete=models.CASCADE)
    start_date=models.DateField(auto_now_add=True)
    price=models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Subscriptions'
    
    def __str__(self):
        return self.user.username
    
#trainer model
class Trainer(models.Model):
    full_name = models.CharField(max_length=150)
    UserName = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    img = models.ImageField(upload_to='trainer/')
    salary=models.IntegerField(default=0)
    facebook=models.CharField(max_length=150, null=True, blank=True)
    instagram=models.CharField(max_length=150, null=True, blank=True) 
    twitter=models.CharField(max_length=150, null=True, blank=True)
    youtube=models.CharField(max_length=150, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Trainers'
    def __str__(self):
        return self.full_name
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))
    
    #notification model
class Notification(models.Model):
    notify_detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    read_by_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)
    read_by_user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return self.notify_detail
    
#notify user model
class NotifyUser(models.Model):
    notify=models.ForeignKey(Notification, on_delete=models.CASCADE)
    read_by_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Notify Users'


    def __str__(self):
        return f"Notification for {self.read_by_user.username}: {self.notify.notify_detail[:30]}"

    
    
    
    #assign subcribers to Trainer
class AssignSubcribers(models.Model):
   
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Assign Subscribers'
    
   
    def __str__(self):
        return f"{self.user} - {self.trainer}"


#trainer achievements model
class TrainerAchievements(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to='trainer_achievements/')
    
    class Meta:
        verbose_name_plural = 'Trainer Achievements'
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80"/>' % (self.img))
    
    
    #trainer salary model
class TrainerSalary(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Trainer Salary'
    
    def __str__(self):
        return f"{self.trainer} - {self.amount}"