'''
Created on Apr 10, 2017

@author: kkuser
'''

class Utils:
    """
    Utils class to provide helper functions
    """
    def get_topic_dict(self, topic):
        """
        Method to convert the object to dict
        :param topic: topic object to be converted to dict
        :returns: dict format of the object
        """
        return {"title": topic.title,
                "sub_redit": topic.sub_reddit,
                "upvotes": topic.upvotes,
                "downvotes": topic.downvotes,
                "user_created": topic.user_created,
                "id": topic.titleid,
                "created_date": str(topic.created_date.date()),
                "topic_type":topic.topic_type}
    
    def sort_topics(self, topics):
        """
        Method to sort the topics on descending order of upvotes
        :param topics: list of topic dicts that have to be sorted.
        :returns: sorted list of topics
        """
        return sorted(topics, key=lambda k: k['upvotes'], reverse=True)
