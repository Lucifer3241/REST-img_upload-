from rest_framework import serializers
from .models import Airport

class AirportSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Airport
        fields=('__all__')
    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    image_url = serializers.ImageField(required=False)

