from django.contrib.auth import get_user_model
from django.template import loader
from django.http import HttpResponse


User = get_user_model()

def index(request):
    context = {}
    context['segment'] = 'index'
    users = User.objects.all()
    context['no_of_active_users'] = users.filter(is_active=True).count()
    context['no_of_super_users'] = users.filter(is_superuser=True).count()
    context['no_of_staff_users'] = users.filter(is_staff=True).count()
    context['total_no_of_users'] = users.count()
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))
