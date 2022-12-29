from django.http import HttpResponse

from .views import password_generator


def send_OTP(request):
    otp = password_generator()
    return HttpResponse("send")


def verify_OTP(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        if otp == "123456":
            return HttpResponse("verified")
        else:
            return HttpResponse("not verified")
