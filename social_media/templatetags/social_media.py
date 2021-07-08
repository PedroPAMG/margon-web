from django import template
from social_media.models import Social_Media

register = template.Library()

@register.simple_tag
def get_social_media_list():
    social_media = Social_Media.objects.all()
    return social_media
    