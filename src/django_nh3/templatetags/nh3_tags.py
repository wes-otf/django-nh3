import nh3
from django import template
from django.utils.safestring import SafeText, mark_safe

from django_nh3.utils import get_nh3_default_options

register = template.Library()


@register.filter(name="nh3")
def nh3_value(value: str | None, tags: str | None = None) -> SafeText:
    """
    Takes an input HTML value and sanitizes it utilizing nh3,
        returning a SafeText object that can be rendered by Django.

    Accepts an optional argument of allowed tags. Should be a comma delimited
        string (ie. "img,span" or "img")
    """
    if value is None:
        return None

    args = {}

    nh3_args = get_nh3_default_options()
    if tags is not None:
        args = nh3_args.copy()
        args["tags"] = set(tags.split(","))
    else:
        args = nh3_args

    nh3_value = nh3.clean(value, **args)
    return mark_safe(nh3_value)
