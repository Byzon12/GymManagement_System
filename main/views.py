from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from . import models
from . import forms
from .forms import EnquiryForm, SignUp
from .models import GalleryImage
from django.core import mail
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import get_template

import os
import stripe



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
    pricing = models.Subplan.objects.all().order_by('price')
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



