from django.shortcuts import render_to_response
from apps.content.models import Info
# Create your views here.




def infomain(request):
    args = {}
    args['info'] = Info.objects.all()


    return render_to_response('main.html', args)