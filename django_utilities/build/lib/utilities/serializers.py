from rest_framework import serializers

from utilities.models import Aboutus, Faq, Home, Reviews, Services, TeamSingle, Teams,Terms,Privacy, Testimonials, Utilities

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"
        depth=2
class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = "__all__"
        depth=2

class PrivacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Privacy
        fields = "__all__"
        depth=2
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutus
        fields = "__all__"
        depth=3
#dsd
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"
        depth=3
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"
        depth=3
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"
        depth=3
class TestimonialsSerializer(serializers.ModelSerializer):
    #serializer1_data = ReviewsSerializer(source='*')
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Testimonials
        fields = "__all__"
        depth=3
    def get_reviews(self, obj):
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return serializer.data
class TeamSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSingle
        fields = "__all__"
        depth=3
class TeamSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    class Meta:
        model = Teams
        fields = "__all__"
        depth=3
    def get_team(self, obj):
        team = TeamSingle.objects.all()
        serializer = TeamSingleSerializer(team, many=True)
        return serializer.data
class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilities
        fields = "__all__"
        depth=3
