from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pasanaku_groups', views.PasanakuGroupViewSet)
router.register(r'members', views.MemberViewSet)
router.register(r'rounds', views.RoundViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'invitations', views.InvitationViewSet)

urlpatterns = [
    path('pasanaku_groups/', views.PasanakuGroupCreateView.as_view()),
    path('pasanaku_groups/count/', views.pasanaku_group_count),
    path('pasanaku_groups/active_groups/', views.active_pasanaku_groups),
    path('members/', views.MemberCreateView.as_view()),
    path('rounds/', views.RoundCreateView.as_view()),
    path('payments/', views.PaymentCreateView.as_view()),
    path('payments/pay/<int:paid>/<int:group_id>/', views.make_payment),
    path('invitations/', views.InvitationCreateView.as_view()),
]
