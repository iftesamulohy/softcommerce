from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from .models import Aboutus, Faq, Home, Services, Teams,Terms,Privacy, Testimonials, Utilities
from .serializers import AboutSerializer, FaqSerializer, HomeSerializer, PrivacySerializer, ServicesSerializer, TeamSerializer, TermsSerializer, TestimonialsSerializer, UtilitiesSerializer
# Create your views here.
class FaqViews(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    queryset = Faq.objects.all()
class TermsViews(viewsets.ModelViewSet):
    serializer_class = TermsSerializer
    queryset = Terms.objects.all()
class PrivacyViews(viewsets.ModelViewSet):
    serializer_class = PrivacySerializer
    queryset = Privacy.objects.all()
class AboutViews(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = Aboutus.objects.all()

#dsd
class HomeViews(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
class ServiceViews(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
class TestimonialsViews(viewsets.ModelViewSet):
    serializer_class = TestimonialsSerializer
    queryset = Testimonials.objects.all()
class TeamViews(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Teams.objects.all()
class UtilitiesViews(viewsets.ModelViewSet):
    serializer_class = UtilitiesSerializer
    queryset = Utilities.objects.all()