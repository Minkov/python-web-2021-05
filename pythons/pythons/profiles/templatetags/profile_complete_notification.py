from django.template import Library

from pythons.profiles.models import Profile

register = Library()


@register.inclusion_tag('tags/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    user_id = context.request.user.id
    profile = Profile.objects.get(pk=user_id)
    return {
        'is_complete': profile.is_complete,
    }
