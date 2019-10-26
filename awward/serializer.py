from rest_framework import serializers
from .models import ProfileMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileMerch
        fields = ('profile_pic', 'username', 'bio','projects')