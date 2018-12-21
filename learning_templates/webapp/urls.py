from django.urls import path
from webapp import views

#FOR TEMP TAGGING
app_name = 'web_application'


urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]
