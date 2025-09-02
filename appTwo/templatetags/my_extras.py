from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value, arg):
  """
  cuts the 'value' string from arg value(s)
  """
  return value.replace(arg,'')
# register.filters('cut',cut)