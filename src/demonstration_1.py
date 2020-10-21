"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

```plaintext
Input:
image = [
        [1,1,1]
       ,[1,1,0],
        [1,0,1]
        ]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```

Notes:

- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.
"""


# sr,sc, image, new color

# Replacing the color of starting pixel and those connected 4 directionally to the starting pixel if they started with the same
# Pixel as the starting pixel
# Replace also those pixel connection 4 directionaly to the pixels are alreayd 4 drectioanly spread appart to starting pixel

# plan
# want to color the current pixel, and those those in the cardinal direction (n,w,s,e)
# keep track of the # of columns and rows
# Search the cardinal directions of the neighbooor pixels to the starting pixel and also the cardinal direct of those neighb pixels as well
# in this section I want to check whether the pixel are equvalent to starting pixel
# I want to to do this by checking the neighboors of the starting pixel (n,w,s,e)
# I need bounds for the search so keep track of the max rows and max colum
#
def flood_fill(image, sr, sc, new_color):
    """
    Inputs:
    image -> List[List[int]]
    sr -> int
    sc -> int
    new_color -> int

    Output:
    List[List[int]]
    """
    # Your code here
    starting_color = image[sr][sc]
    rows = len(image)
    cols = len(image[0])

    # Based on this info create a helper function that runs recursively so that i performa depth first search
    def dfs(image, sr, sc, starting_color, new_color, rows, columns):
        # base
        if image[sr][sc] == starting_color:
            # we should this pixel then
            image[sr][sc] = new_color
            # lets now search the cardinal directions
            # NORTH (check that were at least in the second row otherwise can check up
            if sr >= 1:
                # check upwards (north) and recursively perform a depth first search, checking alll neighboors for the north neighboor
                # to see if they have the same starting color, if so change it to new colo
                dfs(image, sr - 1, sc, starting_color, new_color, rows, columns)
            # SOUTH
            if sr + 1 < rows:  # check that were within bound
                dfs(image, sr + 1, sc, starting_color, new_color, rows, columns)
            # CHECK EAST SIDE
            if sc + 1 < columns:
                dfs(image, sr, sc + 1, starting_color, new_color, rows, columns)
            # WEST
            if sc >= 1:
                dfs(image, sr, sc - 1, starting_color, new_color, rows, columns)

    dfs(image, sr, sc, starting_color, new_color, rows, cols)
    return image



############
# SOL#1
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    queue = [[sr, sc]]
    preColor = image[queue[0][0]][queue[0][1]]
    lenghR = len(image)  # length of row
    lenghC = len(image[0])  # length of collumn

    if preColor == newColor:  # If the new color has no change, then just return the same image
        return (image)

    while queue:
        image[queue[0][0]][queue[0][1]] = newColor  # update the color value
        temp = queue.pop(0)
        # check the array boundaries and the color values, then add the positions to the queue to iterate
        if ((temp[0] - 1) >= 0) and (image[(temp[0] - 1)][temp[1]] == preColor):
            queue.append([temp[0] - 1, temp[1]])
        if ((temp[0] + 1) < lenghR) and (image[(temp[0] + 1)][temp[1]] == preColor):
            queue.append([temp[0] + 1, temp[1]])
        if ((temp[1] - 1) >= 0) and (image[temp[0]][temp[1] - 1] == preColor):
            queue.append([temp[0], temp[1] - 1])
        if ((temp[1] + 1) < lenghC) and (image[temp[0]][temp[1] + 1] == preColor):
            queue.append([temp[0], temp[1] + 1])

    return (image)
