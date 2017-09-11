from django.conf.urls import url
from app_code import views

urlpatterns = [
 #   url(r'^$',views.HomePageView.as_view()),
	url(r'^$',views.HomePageView.as_view()),
    url(r'^result/$',views.ResultPageView.as_view()),
]
