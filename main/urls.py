
from django.urls import path
from . import views

urlpatterns = [
		path('', views.homepage, name = "homepage"),
		path('sent', views.messageSent, name = "message sent"),
		path('privacy-policy', views.privacy, name="privacy policy"),
		path(r'<slug:slug>', views.error404, name = "error404")
]	