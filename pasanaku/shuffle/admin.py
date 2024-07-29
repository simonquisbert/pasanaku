from django.contrib import admin
from .models import PasanakuGroup, Member, Round, Payment, Invitation

class PasanakuGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'bet', 'payment_day', 'rounds', 'created_by', 'created_at', 'updated_at')
    list_display_links = ('name',)
    list_filter = ('created_by',)
    search_fields = ('name', 'description')
    list_per_page = 20

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'join_date')
    list_display_links = ('user',)
    list_filter = ('group',)
    search_fields = ('user__username', 'group__name')
    list_per_page = 20

class RoundAdmin(admin.ModelAdmin):
    list_display = ('order', 'received', 'received_date')
    list_display_links = ('order',)
    list_filter = ('group',)
    search_fields = ('group__name', 'order')
    list_per_page = 20

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'payment_date')
    list_display_links = ('amount',)
    list_filter = ('member', 'round')
    search_fields = ('member__user__username', 'round__group__name')
    list_per_page = 20
    
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'invited_by', 'invited_at', 'accepted', 'accepted_at')
    list_display_links = ('email',)
    list_filter = ('invited_by', 'accepted')
    search_fields = ('email', 'invited_by__username')
    list_per_page = 20

admin.site.register(PasanakuGroup ,PasanakuGroupAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Round, RoundAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Invitation, InvitationAdmin)

