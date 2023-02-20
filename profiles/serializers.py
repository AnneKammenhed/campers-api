from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    """
    Lists all the fields of the camper profiles.
    """
    class Meta:
        model = Profile
        fields = '__all__'
