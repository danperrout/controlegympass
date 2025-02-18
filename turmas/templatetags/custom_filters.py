from django import template

register = template.Library()

@register.filter
def paid_count(presenca_list):
    """
    Conta quantas presenças possuem o atributo 'pago' como True.
    """
    return sum(1 for presenca in presenca_list if presenca.pago)

@register.filter
def attendance_count(presenca_list):
    """
    Conta quantas presenças possuem o atributo 'presente' como True.
    """
    return sum(1 for presenca in presenca_list if presenca.presente)


@register.filter
def subtract(value, arg):
    """Subtrai arg de value."""
    return value - arg
