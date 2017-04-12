'''
Created on Apr 9, 2017

@author: kkuser
'''
import datetime
from Reddit.utils import Utils


def get_initial_topics():
    """
    Method to furnish the initial data. Populated with 21 topics.
    But only the top 20 will be displayed.
    """
    try:
        utils_obj = Utils()
        text_list = ["Music is all to me",
                     "NASA unveiled new plans for getting humans to Mars, and hardly anyone noticed",
                     "20 years ago today, Third Eye Blind released their self-titled album including Jumper and Semi-Charmed Life",
                     "U.S. Navy strike group to move toward Korean peninsula: U.S. official",
                     "CItizens of Krakow have built a hive for 1500 bees in the middle of the city",
                     "'Sons of Guns' star Will Hayden found guilty in sexual assaults of 2 girls; sentenced to life in prison",
                     "A public relations disaster for United Airlines is transforming into an international incident in one of its most important markets",
                     "United CEO doubles down in email to employees, says passenger was 'disruptive and belligerent'",
                     "In 2012, United Airlines Employees Called Disabled Vet 'retard' & Abused His Service Dog",
                     "Trump voters will talk about Hillary even when Trump ends up killing us all.",
                     "United Airlines stock down over 5% premarket trading",
                     "On this date in 1961, Yuri Gagarin became the first human to journey into outer space. Happy Yuri's Night!",
                     "Doctor does all he can to get to patients before being forced off United flight",
                     "Tennessee Could Give Taxpayers America's Fastest Internet For Free, But It Will Give Comcast and AT&T $45 Million Instead",
                     "Stephen Colbert throws staff pizza parties when he beats Jimmy Fallon's ratings.",
                     "The Fast and the Furious movies that feature Corona being consumed average $250 million domestically and have a 63% combined IMDb/RT score. The Fast movies that don't feature Corona average $163 million domestically and have a 57% RT/IMDb average.",
                     "Don't donate to wildlife charities, instead just hand the money straight to the animals so that the business doesn't get a cut of the cash",
                     "Donald Trump proposes marriage to Melania, 2004",
                     "Does pupil constriction only happen when your eye is exposed to light in the visible spectrum?",
                     "Gif used by Wikipedia to explain how cats always land on their feet",
                     "New research suggests California's weather is defying the odds. Meteorologists expected precipitation debts accrued during California's historic drought to last decades, but a new analysis suggests the debts could be erased this year.",
                     ]
        
        topic_type = ["Music", "Space", "Music", "Army", "Public", "Movie", "World News", 
                      "World News", "News", "Politics", "Business", "Facts", "News", "World",
                      "Entertainment", "Entertainment", "Comedy", "History",
                      "Question", "Random", "World"]
        topics = []
        
        
        for i in range(21):
            temp_topic = Topic("Temp topic", "", "admin", "trending")
            temp_topic.upvotes = i
            temp_topic.downvotes = i-1
            temp_topic.title = text_list[i]
            temp_topic.topic_type = topic_type[i]
            temp_topic.titleid = i*10 + 1
            temp_topic.created_date = datetime.datetime(2017,1,1)
            topics.append(temp_topic)
        return topics
    except Exception as exce:
        raise exce

class Topic:
    """
    Class to initialize a topic
    """
    def __init__(self, title, sub_reddit, user_created, topic_type, id=None):
        self.titleid = id
        self.title = title
        self.sub_reddit = sub_reddit
        self.upvotes = 0
        self.downvotes = 0
        self.user_created = user_created
        self.topic_type = topic_type
        self.created_date = datetime.datetime.now()
    
    def track_votes(self, vote_category):
        """
        Method to increment or increment upvotes and downvotes
        :param: vote category(upvotes/downvotes) that has to be tracked
        :returns: None
        """
        if vote_category == "upvotes":
            self.upvotes += 1;
        else:
            self.downvotes += 1;

        