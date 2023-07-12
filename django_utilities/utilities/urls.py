from django.urls import path
from utilities import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'faqs',views.FaqViews,basename="faqs")
router.register(r'terms',views.TermsViews,basename="terms")
router.register(r'privacy',views.PrivacyViews,basename="privacy")
router.register(r'about-us',views.AboutViews,basename="about-us")

router.register(r'index',views.HomeViews,basename="index")
router.register(r'services',views.ServiceViews,basename="services")
router.register(r'testimonials',views.TestimonialsViews,basename="testimonials")
router.register(r'teams',views.TeamViews,basename="teams")
router.register(r'util',views.UtilitiesViews,basename="util")

urlpatterns = [
    
]
urlpatterns+= router.urls