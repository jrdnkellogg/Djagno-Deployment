from django import templates

register = template.Library()


@register.filter(name='cut')
#using a decorator is cleaner than what is used on line 16
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!

    """
    return value.replace(arg,'')


# register.filter('cut',cut)
