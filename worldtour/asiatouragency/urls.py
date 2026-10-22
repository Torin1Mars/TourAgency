from django.urls import path

from .views import home, register_view, home_view, logging_view, logout_view

urlpatterns = [
    path('', home_view, name = "home"),
    path('login/', logging_view, name = "protected"),
    path('logout/', logout_view, name = "logout"),

    #path('contact/', contact_view, name = "contact"),
    #path('contact-success/', contact_success_view, name = "contact_success")
]