from django.http import HttpResponse,HttpResponseRedirect
import urllib

import re


class RequestMiddleware():
    def process_request(self, request):
        try:
            url_keyword = request.META['HTTP_HOST'].split('.')[1]
            url_keyword = re.sub(r"[^\w\s]", '+', url_keyword)
            return HttpResponseRedirect('http://localhost:8000/newscred/?%s' % urllib.urlencode({'query_string':url_keyword}))
        except:
            return None
