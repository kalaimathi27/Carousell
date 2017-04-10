'''
Created on Apr 9, 2017

@author: kkuser
'''
import datetime
from Reddit.utils import Utils


def get_initial_topics():
    try:
        utils_obj = Utils()
        text_list = ["Music is all to me",
                     "NASA unveiled new plans for getting humans to Mars, and hardly anyone noticed",
                     "20 years ago today, Third Eye Blind released their self-titled album including Jumper and Semi-Charmed Life",
                     "U.S. Navy strike group to move toward Korean peninsula: U.S. official",
                     "CItizens of Krakow have built a hive for 1500 bees in the middle of the city",
                     "'Sons of Guns' star Will Hayden found guilty in sexual assaults of 2 girls; sentenced to life in prison"]
        topic_type = ["Music", "Space", "Music", "Army", "Public", "Movie"]
        topics = []
        
        
        for i in range(5):
            temp_topic = Topic("Temp topic", "", "", "admin", "trending")
            temp_topic.upvotes = i
            temp_topic.downvotes = i-1
            temp_topic.title = text_list[i]
            temp_topic.topic_type = topic_type[i]
            temp_topic.titleid = i*10 + 1;
            topics.append(temp_topic)
        return topics
    except Exception as exce:
        raise exce

class Topic:
    """
    Class to initialize a topic
    """
    def __init__(self, title, text, sub_reddit, user_created, topic_type, id=None):
        self.titleid = id
        self.title = title
        self.text = text
        self.sub_reddit = sub_reddit
        self.upvotes = 0
        self.downvotes = 0
        self.user_created = user_created
        self.topic_type = topic_type
        self.created_date = datetime.datetime.now()
    
    def track_votes(self, vote_category):
        if vote_category == "upvotes":
            self.upvotes += 1;
        else:
            self.downvotes -= 1;

        