from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

import re

register = Library()


@register.filter(needs_autoescape=True)
@stringfilter
def nbsp(text, autoescape=None):
    """Converts white space to non-breaking spaces

    This creates a template filter that converts white space to html non-breaking
    spaces. It uses conditional_escape to escape any strings that are incoming
    and are not already marked as safe.
    """
    if autoescape:
        esc = conditional_escape
    else:
        # This is an anonymous python identity function. Simply returns the
        # value of x when x is given.
        esc = lambda x: x
    return mark_safe(re.sub('\s', '&nbsp;', esc(text.strip())))


@register.filter(needs_autoescape=True)
@stringfilter
def v_wrapper(text, autoescape=None):
    """Wraps every v. in a string with a class of alt"""
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(re.sub(' v\. ', '<span class="alt bold"> v. </span>', esc(text)))


@register.filter(needs_autoescape=True)
@stringfilter
def underscore_to_space(text, autoescape=None):
    """Removed underscores from text."""
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(re.sub('_', ' ', esc(text)))


@register.filter(needs_autoescape=True)
@stringfilter
def compress_whitespace(text, autoescape=None):
    """Compress whitespace in a string as a browser does with HTML

    For example, this:
    text   foo

    bar    baz
    bcomes: 'text foo bar baz'
    """
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(' '.join(text.split()))



@register.filter(needs_autoescape=True)
@stringfilter
def naturalduration(seconds, autoescape=None):
    """Convert a duration in seconds to a duration in hours, minutes, seconds.

    For example:
        61 --> 1:01
        3602 --> 1:00:02
    """
    seconds = int(seconds)
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    hours = seconds / 3600
    minutes = seconds % 3600 / 60
    seconds = seconds % 3600 % 60
    time_str = '%02d:%02d:%02d' % (hours, minutes, seconds)
    return mark_safe(time_str.lstrip('0:'))
