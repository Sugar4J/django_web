__author__ = 'candy'
from django.http import HttpResponse
import  datetime
from django.http import Http404
from appDemo import models
import  simplejson
def current_datetime(request,offset):
    try:
        offset = int(offset)
    except Exception as e:
        raise Http404
    now = datetime.datetime.now()
    response_data = models.Book.objects.all()

   # html = "<html><body>It is now %s,%s hours later closed</body></html>" % (now,offset)
    return HttpResponse(simplejson.dumps(response_data),content_type="application/json")

def display_mate(request):
    headers = request.META.items()
    headers.sort()
    html=[]
    for k,v in headers:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table border="1px">%s</table>' %'\n'.join(html))
