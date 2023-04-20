from django.shortcuts import render
from django.http import HttpResponse
from users.models import User, Image

def sign_up(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        otp = request.POST.get('otp')
        name = request.POST.get('name')
        if otp == '00000':
            user, created = User.objects.get_or_create(mobile=mobile, name=name)
            return HttpResponse('User successfully signed up')
        else:
            return HttpResponse('Invalid OTP')
    return render(request, 'sign_up.html')

def sign_in(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        otp = request.POST.get('otp')
        if otp == '00000':
            user = User.objects.get(mobile=mobile)
            return HttpResponse('Welcome ' + user.name)
        else:
            return HttpResponse('Invalid OTP')
    return render(request, 'sign_in.html')


def rate_images(request):
    images = Image.objects.all()
    return render(request, 'rate_images.html', {'images': images})