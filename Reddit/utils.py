'''
Created on Apr 10, 2017

@author: kkuser
'''

class Utils:
    def get_topic_dict(self, topic):
#         import pdb;pdb.set_trace()
        return {"title": topic.title,
                "sub_redit": topic.sub_reddit,
                "upvotes": topic.upvotes,
                "downvotes": topic.downvotes,
                "user_created": topic.user_created,
                "id": topic.titleid,
                "created_date": str(topic.created_date.date()),
                "topic_type":topic.topic_type}
    
    def sort_topics(self, topics):
        return sorted(topics, key=lambda k: k['upvotes'], reverse=True)