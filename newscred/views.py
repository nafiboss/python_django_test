from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from newscred.models import Topic

from newscred.fetcher import Fetcher

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout


def get_edited_topic_name(guid):
    try:
        topic = Topic.objects.get(guid = guid)
        return  topic.group
    except :
        return None

def index(request):
    query_string = request.GET.get('query_string', '')

    topics = None
    if query_string:
      topics = Fetcher.search_topics(Fetcher(), query_string)

    if topics:
        for index, val in enumerate(topics):
            title =  get_edited_topic_name(val['guid'])
            if title:
                topics[index]['topic_group'] = title

    data = {'topics' : topics}
    context = RequestContext(request)
    context.update(data)

    return render_to_response('newscred/index.html', context)

#@cache_page( 60 * 10 )
def detail(request, topic_id):
    topic = Fetcher.search_topic(Fetcher(), topic_id)

    saved_topic = Topic.objects.filter(guid = topic_id).exists()

    if saved_topic:
        saved_topic = Topic.objects.get(guid = topic_id)
        topic['topic_group']  = saved_topic.group

    if not topic:
        raise Http404

    related_topics = Fetcher.search_related_topics(Fetcher(), topic_id)

    data = {'topic' : topic, 'related_topics' : related_topics}
    context = RequestContext(request)
    context.update(data)

    return render_to_response('newscred/detail.html', context)

def save_edited_topic(request):
    topic =   Topic(group  = request.GET.get('title', ''),
                    guid = request.GET.get('guid', ''))
    topic.save()

    return HttpResponse('data saved')

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')