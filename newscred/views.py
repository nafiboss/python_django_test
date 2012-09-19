from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.http import Http404

from newscred.fetcher import Fetcher

def index(request):
    query_string = request.GET.get('query_string', '')

    topics = None
    if query_string:
      topics = Fetcher.search_topics(Fetcher(), query_string)

    return render_to_response('newscred/index.html', {'topics' : topics})

@cache_page( 60 * 10 )
def detail(request, topic_id):
    topic = Fetcher.search_topic(Fetcher(), topic_id)

    if not topic:
        raise Http404

    related_topics = Fetcher.search_related_topics(Fetcher(), topic_id)

    return render_to_response('newscred/detail.html', {'topic' : topic, 'related_topics' : related_topics})