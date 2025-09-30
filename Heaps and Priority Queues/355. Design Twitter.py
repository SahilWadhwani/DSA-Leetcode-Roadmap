"""
LeetCode: 355. Design Twitter
Difficulty: Medium
Link: https://leetcode.com/problems/design-twitter/

Approach:
---------
We simulate a miniature Twitter by tracking:
1. A global timestamp to maintain tweet recency.
2. A dictionary mapping users to their tweets.
3. A dictionary mapping users to the set of users they follow.

To build the news feed:
- We ensure the user follows themself.
- We collect up to 10 tweets from each followee.
- We push all candidate tweets into a **min-heap of size 10**, popping out older tweets to keep only the most recent.

Operations:
- postTweet: O(1)
- getNewsFeed: O(N log K), where N = number of followees × 10, K = 10
- follow/unfollow: O(1)
"""

class Twitter:

    def __init__(self):
        self.time = 0  # global timestamp to track recency
        self.tweets = defaultdict(list)      # userId -> list of (timestamp, tweetId)
        self.follows = defaultdict(set)      # userId -> set of followeeIds     

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Record the tweet with current timestamp
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # Make sure the user follows themself
        self.follows[userId].add(userId)

        # Collect latest tweets from each followee (last 10 tweets per user)
        for followeeId in self.follows[userId]:
            for tweet in self.tweets[followeeId][-10:]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)

        # Return tweets sorted by recency (most recent first)
        result = [tweetId for (_, tweetId) in sorted(heap, reverse=True)]
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId)
