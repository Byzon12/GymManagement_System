from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import login
from . import models
from . import forms
from .forms import EnquiryForm, SignUp
from .models import GalleryImage
from django.core import mail
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from datetime import timedelta
import main.forms as forms




import os
import stripe
from django.db.models import Count



# Create your views here.
#def home(request):
 #   return render(request, 'home.html')

from django.http import HttpResponse
from . import models
def home(request):
    banners=models.Banners.objects.all()
    Services=models.Services.objects.all()[:3]
    images = models.GalleryImage.objects.all().order_by('-id')[:9]
    #return HttpResponse("Welcome to Gym Management System!")
    return render(request, 'home.html', {'banners':banners, 'services':Services , 'images':images})
  
  #page detail
def page(request, id):
    page=models.Page.objects.get(id=id)
    return render(request, 'page.html', {'page':page})


# ✅ View for a specific page


#fqa
def fqa(request):
    fqa=models.Fqa.objects.all()
    return render(request, 'fqa.html', {'fqa':fqa})
  
#query
def Enquiry(request):
  form = EnquiryForm()
  msg = ''
  if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Form submission successful'
           
        else:
            msg = 'Form is not valid'
  return render(request, 'Enquiry.html', {'form':form, 'msg':msg})

#gallery
def gallerys(request):
    galleries = models.Gallery.objects.all().order_by('-id')
    return render(request, 'Gallery.html', {'galleries':galleries, 'gallery':galleries})

   
    #gallery image
def gallery_detail(request, id):
    gallery = get_object_or_404(models.Gallery, id=id)
    gallery_img = GalleryImage.objects.filter(gallery=gallery)
    return render(request, 'gallary_img.html', {'gallery_img':gallery_img, 'image':gallery_img})

#subcription plan
def pricing(request):
    pricing = models.Subplan.objects.annotate(total_members=Count('id')).all().order_by('price')
   
    dfeatures = models.Subfeature.objects.all()
    # Remove duplicates before passing to the template
    unique_features = {feature.title: feature for feature in dfeatures}.values()

# Pass unique_features instead of dfeatures to the template

    return render(request, 'pricing.html', {'plans':pricing, 'dfeatures':dfeatures, 'unique_features':unique_features})

#signup
def SignUp(request):
    msg = ''
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        if form.is_valid():
            form.save()
            msg = 'User created'
        else:
            msg = 'Form is not valid'
    form =forms.SignUp()
    return render(request, 'registration/signup.html', {'form': form, 'msg': msg})

#checkout
def Checkout(request, plan_id):
    planDetail = models.Subplan.objects.get(pk=plan_id)
    
    return render(request, 'checkout.html', {'plan': planDetail})

#stripe
stripe.api_key =('sk_test_51QujVaG2JjFRWwN01QI0HL5mNwGJWaotOeJn8FvynMuedQ4z9JETsitPywGN3Qr8r2OB60dcjSkqeYGyKZKIp96b00KFQwTo4r')
def checkout_session(request, plan_id):
    plan = models.Subplan.objects.get(pk=plan_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': plan.title,
                },
                'unit_amount': int(float(plan.price)*100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://127.0.0.1:8000/pay_cancel',
        client_reference_id=plan_id
    )
    return redirect(session.url, code=303)

#success
def pay_success(request):
    session = stripe.checkout.Session.retrieve(request.GET.get('session_id'))
    plan_id=session.client_reference_id
    plan = models.Subplan.objects.get(pk=plan_id)
    user=request.user
    models.Subscription.objects.create(
        plan=plan,
        user=user,
        price=plan.price,
        
    )
    # Email details
    from_email = 'byzoneochieng@gmail.com'  # Your email
    to = user.email  # Recipient's email
    subject = 'Subscription Successful'  

    # Construct the plain text email content
    email_body = f"""
    Hello {user.username},
    
    Your subscription to {plan.title} was successful.

    Details:
    - Name: {user.username}
    - Email: {user.email}
    - Plan: {plan.title}
    - Amount Paid: ${plan.price}

    Thank you for your subscription!

    Regards,
    Gym Management System Team
    """

    # Send email
    msg = EmailMessage(subject, email_body, from_email, [to])
    msg.send()

    return render(request, 'success.html', {'session': session, 'plan_id': plan_id})
    
    

#cancel
def pay_cancel(request):
    return render(request, 'cancel.html')

#USER DASHBOARD
def userdashboard(request):
    current_plan=models.Subscription.objects.get(user=request.user)
    my_trainer=models.AssignSubcribers.objects.filter(user=request.user).first()
    end_date = current_plan.start_date + timedelta(days=current_plan.plan.validity_days)
   

 #notification
    totalUnread = 0
    # Get all notifications for the logged-in user
    # Assuming you have a Notification model with a ManyToMany relationship to User
    notifications = models.Notification.objects.all().order_by('-id')
   
    for notification in notifications:
        notify_status = models.NotifyUser.objects.filter(
            notify=notification,
            read_by_user=request.user
        ).exists()
        if notify_status:
            notify_status = True
        if not notify_status:
            totalUnread += 1
    return render(request, 'userdashboard.html', {'current_plan': current_plan, 'my_trainer': my_trainer, 'notifications': notifications, 'totalUnread': totalUnread, 'end_date': end_date})

   

#edit form
def update_profile(request):
    msg= None

    if request.method == 'POST':
        form = forms.profileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            msg = 'Profile updated successfully'
        
    form = forms.profileForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

#change password
def change_password(request):
    msg = None
    if request.method == 'POST':
        form = forms.PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Password updated successfully'
            login(request, user)
        else:
            msg = 'Please correct the error below.'
    else:
        form = forms.PasswordChangeForm(request.user)
    return render(request, 'registration/passwordchange.html', {'form': form, 'msg': msg})

#trainer login
def trainer_login(request):
    msg = None
    if request.method == 'POST':
        form = forms.TrainerLoginForm(request.POST)
        if form.is_valid():
            UserName = form.cleaned_data['UserName']
            password = form.cleaned_data['password']
            trainer= models.Trainer.objects.filter(UserName=UserName, password=password).count()
            if trainer>0:
                request.session['traioerLogin']= True
                trainer=models.Trainer.objects.filter(UserName=UserName, password=password).first()
                
                return redirect('trainer_dashboard')
                msg = 'Login successful'
    else:
        msg = 'Invalid username or password'
        form = forms.TrainerLoginForm()
    return render(request, 'trainer/login.html', {'form': form, 'msg': msg})

#trainer logout
def trainer_logout(request):
    if request.session.get('traionerLogin'):
        del request.session['traionerLogin']
    return redirect('home')

#trainer Dashboard
def trainer_dashboard(request):
    return render(request, 'trainer/userDashboard.html')

#trainer profile
def trainer_profile(request):
    if not request.session.get('trainerLogin'):
        return redirect('trainer_login')
    
    if request.method.POST:
        form = forms.TrainerProfileForm(request.POST, instance=trainer_dashboard)
        if form.is_valid():
            form.save()
            msg = 'Profile updated successfully'
    form = forms.TrainerProfileForm
    
    return render(request,"trainer/trainer_profile.html", {'form': form})

#notification
def notification(request):
    if request.user.is_authenticated:
        notifications = models.Notification.objects.all().order_by('-id')
        return render(request, 'notification.html', {'notifications': notifications})
    else:
        return redirect('login')
    
# def notification(request):


def get_notifications(request):
    if request.user.is_authenticated:
        totalUnread =0
        # Get all notifications for the logged-in user
        # Assuming you have a Notification model with a ManyToMany relationship to User
        notifications = models.Notification.objects.all().order_by('-id')
        jsonData = []
        for notification in notifications:
                notify_status = models.NotifyUser.objects.filter(
                    notify=notification,
                    read_by_user=request.user
                ).exists()
                if notify_status:
                    notify_status = True
                if not notify_status:
                    totalUnread += 1

                jsonData.append({
                    'id': notification.pk,
                    'notify_detail': notification.notify_detail,
                    'date': notification.date,
                    'status': notify_status,
                    
                })
        notification.save()
       # data = serializers.serialize('json', notifications)
        #data = serializers.serialize('json', notifications)
       
        return JsonResponse({
            'totalUnread': totalUnread,
            'notifications': jsonData
        }, safe=False)
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)  
    
    
    
  #notification read by user
@csrf_protect
@require_POST
@csrf_exempt
def mark_notification_as_read(request):
    if request.method == 'POST':
        notification_id = request.POST.get('notification')
        if notification_id:
            try:
                notification = models.Notification.objects.get(pk=notification_id)
                # Assuming NotifyUserStatus is your model to mark read
                notify_user = models.NotifyUser.objects.create(
                    notify=notification,
                    read_by_user=request.user,
                   
                )
                notify_user.save()
                return JsonResponse({'status': 'success'})
            except models.Notification.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Notification not found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'message': 'Notification ID not provided'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
