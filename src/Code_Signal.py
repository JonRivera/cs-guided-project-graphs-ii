# There are N students in a baking class together. Some of them are friends,
# while some are not friends. The students' friendship can be considered transitive. This means that if Ami is a direct
# friend of Bill, and Bill is a direct friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group
# of students who are either direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationships between students in the class.
# If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
#
# You need to write a function that can output the total number of friend circles among all the students.


# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation: The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # len of
        visited = [0] * len(M)
        friend_circle = 0  # not 0 === True, 0 == False

        for i in range(len(M)):
            if not (visited[i]):
                visited[i] = 1
                friend_circle += 1
                queue = [i]
                while queue:
                    popi = queue.pop(0)
                    visited[popi] = 1
                    for j in range(len(M)):
                        if not (visited[j]) and M[popi][j] == 1:
                            queue.append(j)
                            visited[j] = 1

        return friend_circle


"""OTHER SOLUTION"""
from collections import deque


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # dimension of M = the no of people
        N = len(M)

        # list of people whos relationships have been check
        visited = set()

        # no of distinct circles
        noofcircles = 0

        def bfs(level):
            nextlevel = set()

            while (level):
                f = level.popleft()

                # add i to visited set
                visited.add(f)

                for i in range(N):
                    if i != f and M[f][i] == 1 and i not in visited:
                        nextlevel.add(i)

            if len(nextlevel) != 0:
                bfs(deque(nextlevel))

        # main
        for i in range(N):
            if i not in visited:
                noofcircles += 1
                bfs(deque([i]))

        return noofcircles

# Thorough Explanation of Solution to the Problem
# https://www.educative.io/edpresso/the-friend-circle-problem
