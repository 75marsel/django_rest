from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "card_title",
            "card_text", 
            "card_email", 
            "card_link",
            "card_footer",
            "card_username",
        ]
        
        