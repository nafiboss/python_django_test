import urllib2
import json


class Fetcher:
    base_url = 'http://api.newscred.com/'
    access_key = 'c4bcc3f7c9bf9ec159f51da0a86ca658'
    format = 'json'

    def fetch(self, request_url):
        http_response  = urllib2.urlopen(request_url).read()
        return json.loads(http_response)


    def search_topics(self, query_string):
        topics_request_url = '%s/topics?access_key=%s&format=%s&query=%s' % (self.base_url, self.access_key, self.format, query_string)
        json_data = Fetcher.fetch(Fetcher(), topics_request_url)
        return json_data.get('topic_set', None)


    def search_related_topics(self, guid):
        related_topics_request_url = '%s/topic/%s/topics?access_key=%s&pagesize=10&format=%s' % (self.base_url, guid, self.access_key, self.format)
        json_data = Fetcher.fetch(Fetcher(), related_topics_request_url)
        return json_data.get('topic_set', None)

    def search_topic(self, guid):
        topic_request_url = '%s/topic/%s?access_key=%s&format=%s' % (self.base_url, guid, self.access_key, self.format)
        json_data = Fetcher.fetch(Fetcher(), topic_request_url)
        return  json_data.get('topic', None)



