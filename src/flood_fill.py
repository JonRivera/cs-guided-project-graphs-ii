"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).  ###[12]

Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the ********starting pixel,
 lus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

```plaintext
Input:
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
sr = 1, sc = 1, newColor = 2
Output: [
    [2,2,2],
    [2,2,0],
    [2,0,1]
]
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
    # from the starting pixel, "radiate" out from it, coloring all pixels 
    # that match the color of our starting pixel to `new_color`
    # do this by checking all 4 cardinal directions from our starting pixel 

    # should we opt for DFS or BFS? 
    # Probably doesn't matter, since we don't really care what order the 
    # pixels get colored in 

    # what's the criteria for knowing that a pixel should not be colored in? 
    # if the pixel's color does not match the color of the initial starting pixel 

    # 1. note the color of the starting position pixel 
    initial_color = image[sr][sc]
    rows = len(image)
    cols = len(image[0])
    # I want to create some helper function that takes this info
    # And performs a depths first search
    dft(image, sr, sc, initial_color, new_color, rows, cols)

    return image


def dft(image, sr, sc, initial_color, new_color, rows, cols):
    # 2. set the starting pixel to `new_color` if its initial color == `initial_color`
    if image[sr][sc] == initial_color:
        image[sr][sc] = new_color
        # 3. look in all 4 directions from the starting pixel
        # look north
        if sr >= 1:
            dft(image, sr - 1, sc, initial_color, new_color, rows, cols)
        # look south 
        if sr + 1 < rows:
            dft(image, sr + 1, sc, initial_color, new_color, rows, cols)
        # look east 
        if sc + 1 < cols:
            dft(image, sr, sc + 1, initial_color, new_color, rows, cols)
        # look west 
        if sc >= 1:
            dft(image, sr, sc - 1, initial_color, new_color, rows, cols)

    # 4. for each pixel whose color matches the initial color of the starting pixel 
    # 5. set it to `new_color` 
    # 6. recurse, passing in this pixel into our recursive function 


image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

print(flood_fill(image, 1, 1, 2))
