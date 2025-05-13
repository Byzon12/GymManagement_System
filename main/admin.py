#from tkinter import PAGES
from django.contrib import admin
from . import models
from .models import Banners,Services, Page, Fqa, Enquiry, Gallery, GalleryImage, Subplan, Subfeature, PlanDiscount, Subscribers, Subscription, Trainer,TrainerSalary, Notification, NotifyUser, AssignSubcribers, TrainerAchievements
from django.db import models
from django.contrib import admin
from django.contrib import admin

from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# Register your models here.
class BannersAdmin(admin.ModelAdmin):
    list_display = ['alt_text', 'image_tag']
    #readonly_fields = ['image_tag']
admin.site.register(Banners, BannersAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
   # readonly_fields = ['image_tag']
admin.site.register(Services, ServicesAdmin)

#page admin
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
admin.site.register(Page, PageAdmin)

#fqa admin
class FqaAdmin(admin.ModelAdmin):
    list_display = ['question']
admin.site.register(Fqa, FqaAdmin)

#query admin
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'send_date', 'message', 'send_location']
admin.site.register(Enquiry, EnquiryAdmin)

#gaallery admin
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'detail']
admin.site.register(Gallery, GalleryAdmin)

#gallery image admin
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'image_tag','alt_text']
admin.site.register(GalleryImage, GalleryImageAdmin)

#subscription plan admin
class SubsplanAdmin(admin.ModelAdmin):
    list_editable=['max_member']
    list_display = ['title', 'price', 'detail', 'highlight_status', 'max_member', 'validity_days']
admin.site.register(Subplan, SubsplanAdmin)

#subscription features admin
class SubsfeatureAdmin(admin.ModelAdmin):
    list_display = ['title','suplans']
    def suplans(self, obj):
        return ", ".join([p.title for p in obj.subplan.all()])
    
admin.site.register(Subfeature, SubsfeatureAdmin)

#package discount admin
class PackagediscountAdmin(admin.ModelAdmin):
    list_editable=['total_discount']
    list_display = ['subplan', 'total_month', 'total_discount']
admin.site.register(PlanDiscount, PackagediscountAdmin)

##subcribers admin
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['User', 'email','full_name', 'phone', 'address', 'city',"image_tag"]

admin.site.register(Subscribers, SubscribersAdmin)


#subcription 
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'price', 'start_date']
admin.site.register(Subscription, SubscriptionAdmin)

#trainer admin
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['full_name','UserName','password', 'email', 'phone','salary','address', 'is_active','image_tag']
    list_editable = ['is_active']
admin.site.register(Trainer, TrainerAdmin)

#notification admin
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notify_detail', 'date', 'read_by_trainer', 'read_by_user', 'status']
admin.site.register(Notification, NotificationAdmin)

#notify user admin
class NotifyUserAdmin(admin.ModelAdmin):
    list_display = ['status', 'notify', 'read_by_user']
admin.site.register(NotifyUser, NotifyUserAdmin)

#assignsubcribe admin

class AssignSubcribeAdmin(admin.ModelAdmin):
    list_display = ['user','trainer']
    
admin.site.register(AssignSubcribers, AssignSubcribeAdmin)

#triner achievement admin
class TrainerAchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'trainer','detail','image_tag']
admin.site.register(TrainerAchievements, TrainerAchievementAdmin)

#trainer salary admin
class TrainerSalaryAdmin(admin.ModelAdmin):
    list_display = ['trainer', 'amount', 'date']
#admin.site.register(Trainer, TrainerSalaryAdmin)
admin.site.register(TrainerSalary, TrainerSalaryAdmin)