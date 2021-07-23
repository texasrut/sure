from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quotes import views

urlpatterns = [
    path("v1/quotes/", views.quote_list),
    path("v1/premiums/<str:quote_number>", views.premium_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
