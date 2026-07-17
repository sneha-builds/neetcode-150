# Design Twitter

"""

Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:

  . Twitter() Initializes the twitter object.
  . void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
  . List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following
    or by the user themself. Tweets IDs should be ordered from most recent to least recent.
  . void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
  . void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.

Constraints :
  . 1 <=userId, followerId, followeeId <= 100
  . 0 <= tweetId <= 1000
  
"""


class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweetMap[userId][:]
        for followeeId in self.followMap[userId]:
            feed.extend(self.tweetMap[followeeId])

        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)