from django import template
register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()

@register.simple_tag
def get_quarter_from_num(qt):
    quarter_str = ''
    if qt == 1:
      quarter_str = '春'
    elif qt == 2:
      quarter_str = '夏'
    elif qt == 3:
      quarter_str = '秋'
    elif qt == 4:
      quarter_str = '冬'
    return quarter_str