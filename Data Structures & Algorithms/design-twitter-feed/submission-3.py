class Twitter:

    def __init__(self):
        self.time = 0
        # follower (nguoi theo doi): set of followee (nguoi duoc theo doi)
        self.followMap = defaultdict(set) 
        self.tweetMap = defaultdict(list) # user id : list of tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = list(self.tweetMap[userId])
        for fId in self.followMap[userId]:
            feeds.extend(self.tweetMap[fId])
        
        feeds.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feeds[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
