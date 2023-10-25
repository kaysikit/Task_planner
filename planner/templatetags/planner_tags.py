from django import template
from planner.models import Task, Status

register = template.Library()


@register.simple_tag()
def get_status():
    return Status.objects.all( )