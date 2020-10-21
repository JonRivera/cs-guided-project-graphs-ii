"""
In a town, there are `N` people labelled from `1` to `N`.  There is a rumor
that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given `trust`, an array of pairs `trust[i] = [a, b]` representing that ###NOTE: AT LOCATION I, THIS PERSON TRUSTS THAT PERSON ETC.
the person labelled `a` trusts the person labelled `b`.

If the town judge exists and can be identified, return the label of the town
judge.  Otherwise, return `-1`.

Example 1:

```plaintext
Input: N = 2, trust = [[1,2]]
Output: 2
```

Example 2:

```plaintext
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
```

Example 3:

```plaintext
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

Example 4:

```plaintext
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
```

Example 5:

```plaintext
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
```

Constraints:

- `1 <= N <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- `trust[i]` are all different
- `trust[i][0] != trust[i][1]`
- `1 <= trust[i][0], trust[i][1] <= N`
"""

"""SOL:2 ARRAY ALGORITHIM"""


def find_judge(N, trust):
    """
    Inputs:
    N -> int
    trust -> List[List[int]]

    Output:
    int
    """
    # Your code here  
    # In order for a town to exist, there needs to be one 
    # node that every other node points to, and that node
    trusts_me = [0 for _ in range(
        N + 1)]  # placements for each person : Labels 1 through N => ex) label 1 current is trust by 0 persons
    # at index 0 this element is never going to get updated as there is no label with index
    # the reaon we include the 0 in range(N+1) is that we can match the labels in trustee to truts me 1:1
    # count the number of people who trust each person
    i_trust = [0 for _ in range(N + 1)]
    for truster, trustee in trust:
        trusts_me[
            trustee] += 1  # person(trustee) is getting trusted so add 1 to to trusts me corresponding to that label
        i_trust[truster] += 1  # we want to use the trustee labels as index to update the trusts me array

    # we can check to see if one person's `trust_count` == N - 1 # at most a person can be trusted N-1 times he can't include himself
    for person, trust_count in enumerate(trusts_me):
        if trust_count == N - 1 and i_trust[person] == 0:
            return person

            # we also need to check that this person has no outgoing arrows
    # cannot have any arrows pointing out from it 
    # and there can only be one
    return -1


print(find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
print(find_judge(3, [[1, 2], [2, 3]]))

#####

# Techniques: Indeph,
# Prob -> Graph
# DS: lists
# SY: Use two arrays, that keep track of who is satisfying the conditons of judge or not
# verify if conditions hold
