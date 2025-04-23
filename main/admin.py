#from tkinter import PAGES
from django.contrib import admin
from . import models


# Register your models here.
class BannersAdmin(admin.ModelAdmin):
    list_display = ['alt_text', 'image_tag']
    #readonly_fields = ['image_tag']
admin.site.register(models.Banners, BannersAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
   # readonly_fields = ['image_tag']
admin.site.register(models.Services, ServicesAdmin)

#page admin
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
admin.site.register(models.Page, PageAdmin)

#fqa admin
class FqaAdmin(admin.ModelAdmin):
    list_display = ['question']
admin.site.register(models.Fqa, FqaAdmin)

#query admin
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'send_date', 'message', 'send_location']
admin.site.register(models.Enquiry, EnquiryAdmin)

#gaallery admin
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'detail']
admin.site.register(models.Gallery, GalleryAdmin)

#gallery image admin
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'image_tag','alt_text']
admin.site.register(models.GalleryImage, GalleryImageAdmin)

#subscription plan admin
class SubsplanAdmin(admin.ModelAdmin):
    list_editable=['max_member']
    list_display = ['title', 'price', 'detail', 'highlight_status', 'max_member']
admin.site.register(models.Subplan, SubsplanAdmin)

#subscription features admin
class SubsfeatureAdmin(admin.ModelAdmin):
    list_display = ['title','suplans']
    def suplans(self, obj):
        return ", ".join([p.title for p in obj.subplan.all()])
    
admin.site.register(models.Subfeature, SubsfeatureAdmin)

#package discount admin
class PackagediscountAdmin(admin.ModelAdmin):
    list_editable=['total_discount']
    list_display = ['subplan', 'total_month', 'total_discount']
admin.site.register(models.PlanDiscount, PackagediscountAdmin)

##subcribers admin
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['User', 'email','full_name', 'phone', 'address', 'city',"image_tag"]

admin.site.register(models.Subscribers, SubscribersAdmin)


#subcription 
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'price']
admin.site.register(models.Subscription, SubscriptionAdmin)

