from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Product
from .models import Service
from .models import ContactMessage
from django.contrib import messages
from .forms import ContactForm
from .models import GalleryImage
from .forms import OrderForm
from .models import Order

def home(request):
    return render(request, 'core/home.html')

def about(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'core/about.html', {'gallery_images': gallery_images})

def products_view(request):
    products = Product.objects.all()
    return render(request, 'core/products.html', {'products': products})

def services_view(request):
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # ✅ First extract form data
            full_name = form.cleaned_data['full_name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # ✅ Then save to DB
            ContactMessage.objects.create(
                full_name=full_name,
                mobile=mobile,
                email=email,
                subject=subject,
                message=message,
            )

            # ✅ Then send confirmation email to user
            send_mail(
                subject='Thanks for contacting SMART AGRO TECH',
                message=(
                    f"Dear {full_name},\n\n"
                    f"Thanks for reaching out to SMART AGRO TECH. "
                    "We received your message and will get back to you soon.\n\n"
                    "Regards,\nSMART AGRO TECH Team"
                ),
                from_email='smartagrotechkhulna@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )

            # ✅ Optional: Email to admin (your inbox)
            send_mail(
                subject=f"New Contact Message: {subject}",
                message=(
                    f"Name: {full_name}\n"
                    f"Mobile: {mobile}\n"
                    f"Email: {email}\n\n"
                    f"Message:\n{message}"
                ),
                from_email=email,
                recipient_list=['smartagrotechkhulna@gmail.com'],
                fail_silently=False,
            )

            # ✅ Show success message
            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})


# Placeholder SMS function (replace with actual API call later)
def send_sms(mobile, message):
    print(f"SMS to {mobile}: {message}")  # Replace with actual SMS gateway


def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            # Notification to owner
            send_mail(
                subject="New Order Received",
                message=f"Order from {order.name}, Mobile: {order.mobile}",
                from_email='smartagrotechkhulna@gmail.com',
                recipient_list=['smartagrotechkhulna@gmail.com']
            )
            send_sms('owner-mobile-number', f"New order received from {order.name} ({order.mobile})")

            # Confirmation to user
            if order.email:
                send_mail(
                    subject="Order Placed Successfully",
                    message="Thank you for placing your order with SMART AGRO TECH.",
                    from_email='smartagrotechkhulna@gmail.com',
                    recipient_list=[order.email]
                )
            send_sms(order.mobile, "Your order has been placed successfully. Thank you!")

            messages.success(request, "Your order has been placed successfully!")
            return redirect('order')
    else:
        form = OrderForm()

    return render(request, 'core/order_form.html', {'form': form})



