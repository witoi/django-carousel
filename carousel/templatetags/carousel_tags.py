from django import template

import six

from ..models import Carousel


register = template.Library()

DEFAULT_TEMPLATE_NAMES = ['carousel/templatetags/carousel.html']


def render_carousel(context, template_name):
    template_names = get_template_names(template_name=template_name)
    return template.loader.render_to_string(template_names, context)


def get_template_names(template_name):
    template_names = DEFAULT_TEMPLATE_NAMES
    if template_name:
        template_names.insert(0, template_name)
    return template_names


@register.simple_tag(takes_context=True)
def carousel(context, carousel, template_name=None):
    if isinstance(carousel, six.string_types):
        return carousel_with_name(context, name=carousel, template_name=template_name)
    context['carousel'] = carousel
    return render_carousel(context, template_name)


@register.simple_tag(takes_context=True)
def carousel_with_name(context, name, template_name=None):
    try:
        context['carousel'] = Carousel.objects.get(name=name)
        return render_carousel(context, template_name)
    except Carousel.DoesNotExist:
        return ''


@register.simple_tag(takes_context=True)
def carousel_with_id(context, id, template_name=None):
    try:
        context['carousel'] = Carousel.objects.get(id=id)
        return render_carousel(context, template_name)
    except Carousel.DoesNotExist:
        return ''
