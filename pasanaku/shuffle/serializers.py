from rest_framework import serializers
from .models import PasanakuGroup, Member, Round, Payment, Invitation

class PasanakuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasanakuGroup
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'