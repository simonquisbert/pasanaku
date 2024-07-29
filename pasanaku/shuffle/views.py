from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from .models import PasanakuGroup, Member, Round, Payment, Invitation
from .serializers import InvitationSerializer, PasanakuGroupSerializer, MemberSerializer, PaymentSerializer, RoundSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
class MemberCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

class RoundCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

class InvitationCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

class PasanakuGroupViewSet(viewsets.ModelViewSet):
    queryset = PasanakuGroup.objects.all()
    serializer_class = PasanakuGroupSerializer
    
class PasanakuGroupCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = PasanakuGroup.objects.all()
    serializer_class = PasanakuGroupSerializer
    
@api_view(['GET'])
def pasanaku_group_count(request):
    """
    Cuenta la Cantidad de Grupos del Pasanaku
    """
    try:
        count = PasanakuGroup.objects.count()
        return JsonResponse(
            {
                'count': count
            },
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                'error': str(e)
            },
            safe=False,
            status=400
            )

@api_view(['GET'])
def active_pasanaku_groups(request):
    """
    Cuenta la Cantidad de Grupos activos del Pasanaku
    """
    try:
        active_groups = PasanakuGroup.objects.filter(is_active=True).values('id', 'name', 'bet','rounds','expiration_date','is_active')
        return JsonResponse(
            list(active_groups),
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                'error': str(e)
            },
            safe=False,
            status=400
            )

@api_view(['POST'])
def make_payment(request, paid, group_id):
    """
    Crea un nuevo Pago
    """
    try:
        group = PasanakuGroup.objects.get(id=group_id)
        member = Member.objects.get(user=request.user, group=group)
        round = Round.objects.get(group=group, order=1)
        
        payment = Payment.objects.create(
            member=member,
            round=round,
            amount=paid
        )
        payment.save()
        
        round.received = True
        round.received_date = timezone.now()
        round.save()
        
        return JsonResponse(
            {'success': True},
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {'error': str(e)},
            status=400
        )
    