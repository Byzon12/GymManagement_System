from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ Home page
    path('page/<int:id>/', views.page, name='page'),  # ✅ Detail page with ID
    path('fqa', views.fqa, name='fqa'),
    path('Enquiry', views.Enquiry, name='Enquiry'),
    path('gallerys', views.gallerys, name='gallerys'),
    path('gallery/<int:id>/', views.gallery_detail, name='gallery_detail'),
    path('pricing', views.pricing, name='pricing'),
    path('accounts/signup/', views.SignUp, name='signup'),
    path('Checkou/<int:plan_id>', views.Checkout, name='Checkout'),
    path('checkout_session/<int:plan_id>', views.checkout_session, name='checkout_session'),
    path('pay_success', views.pay_success, name='pay_success'),
    path('pay_cancel', views.pay_cancel, name='pay_cancel'),
    
    #USERDASHBOARD URLS
    path('userdashboard', views.userdashboard, name='userdashboard'),
    path('update_profile', views.update_profile, name='update_profile'),
   path('change_password', views.change_password, name='change_password'),
   #trainer
   path('trainer/login', views.trainer_login, name='trainer_login'),
   path('trainer/logout', views.trainer_logout, name='trainer_logout'),
   path('trainer_dashboard', views.trainer_dashboard, name='trainer_dashboard'),
   path('trainer_profile', views.trainer_profile, name='trainer_profile'),
    
   #notification
    path('notification', views.notification, name='notification'),
    path('get_notification', views.get_notifications, name='get_notification'),
    path('notification/read_by_user', views.mark_notification_as_read, name='read_by_user'),
  

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
