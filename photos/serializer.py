from rest_framework import serializers
from .models import Project
class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'picture_Main_pic','description', 'link')