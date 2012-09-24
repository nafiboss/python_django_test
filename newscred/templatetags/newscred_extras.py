from django import template
from urllib2 import urlopen
from django.utils.safestring import mark_safe
from newscred.fetcher import Fetcher

register = template.Library()


def upper(value):
    return value.upper()


def shorter_url(long_url):
    bitly_url = "http://tinyurl.com/api-create.php?url={0}"
    req_url = bitly_url.format(long_url)
    short_url = urlopen(req_url).read()
    return short_url

register.filter('upper', upper)
register.filter('shorter_url',shorter_url)


class TopicNode(template.Node):
    def __init__(self, guid):
        self.guid = template.Variable(guid)

    def render(self, context):
        self.guid = self.guid.resolve(context)
        topic = Fetcher.search_topic(Fetcher(), self.guid)
        return mark_safe("<div class='topic'><div class='topic_thumb'><img src='%s'/></div>%s<br/>URL: <a href='%s'>%s</a></div>" %
                         (topic['image_url'], topic['description'], topic['link'], topic['link'], ) )


@register.tag(name="topic_detail")
def topic_detail(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, guid = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    return TopicNode(guid)