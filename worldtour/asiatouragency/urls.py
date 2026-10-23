from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_view ,name = "home"),
    path('login/', views.logging_view, name = "login"),
    path('logout/', views.logout_view, name = "logout"),
    path('logout/', views.register_view, name = "register"),

    path('protected/', views.ProtectedView.as_view(), name = "protected"),

    #path('contact/', contact_view, name = "contact"),
    #path('contact-success/', contact_success_view, name = "contact_success")
]