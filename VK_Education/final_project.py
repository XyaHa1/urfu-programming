from typing import List


class Twitter:

    def __init__(self):
        self.tweets = []
        self.followees = {}
        self.timestamp = 0

    def post_tweet(self, user_id, tweet_id):
        self.tweets.append((self.timestamp, user_id, tweet_id))
        self.timestamp += 1

    def get_news_feed(self, user_id) -> List[int]:
        following = self.followees.get(user_id, set())
        following.add(user_id)

        feed = []
        for ts, author_id, tweet_id in reversed(self.tweets):
            if author_id in following:
                feed.append(tweet_id)
                if len(feed) == 10:
                    break
        return feed

    def follow(self, follower_id, followee_id):
        if follower_id not in self.followees:
            self.followees[follower_id] = set()
        self.followees[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        if follower_id in self.followees and followee_id in self.followees[follower_id]:
            self.followees[follower_id].remove(followee_id)
