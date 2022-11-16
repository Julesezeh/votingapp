from rest_framework import serializers
from voting.models import Lga

class LgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lga
        fields = ('lga_id','lga_name',)