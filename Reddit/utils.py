'''
Created on Apr 10, 2017

@author: kkuser
'''

class Utils:
    def get_topic_dict(self, topic):
        return {"title": topic.title,
                "text": topic.text,
                "sub_redit": topic.sub_reddit,
                "upvotes": topic.upvotes,
                "downvotes": topic.downvotes,
                "user_created": topic.user_created,
                "id": topic.titleid}
    
    def sort_topics(self, topics):
        return sorted(topics, key=lambda k: k['upvotes'], reverse=True)