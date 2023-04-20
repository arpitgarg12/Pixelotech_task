from django.urls import path
from users.views import sign_up, sign_in, rate_images

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('sign-in/', sign_in, name='sign_in'),
    path('rate-images/', rate_images, name='rate_images'),
]
