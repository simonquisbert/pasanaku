from django.core.exceptions import ValidationError

def validate_amount(paid_value, expected_paid):
    if paid_value != expected_paid:
        raise ValidationError(r'El valor del pago (${paid_value}) no coincide con el de la cuota (${expected_paid})'.format(paid_value=paid_value, expected_paid=expected_paid))
    
def validate_payment_day(value):
    if value > 14:
        raise ValidationError("El dia de pago no puede pasar de las dos primeras semanas del mes")