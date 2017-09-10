from django.conf.urls import url
from app_code import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view()),
]
