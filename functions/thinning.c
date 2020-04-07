#include <stdio.h>



unsigned char * neighbours(int x, int y, unsigned char **image):
    return  {image[x-1][y], image[x-1][y+1], image[x][y+1], image[x+1][y+1], image[x+1][y], image[x+1][y-1], image[x][y-1], image[x-1][y-1]}    // P2,P3,P4,P5,P6,P7,P8,P9

unsigned int transitions(unsigned char *neighbours):
    //No. of 0,1 patterns (transitions from 0 to 1) in the ordered sequence
    n = neighbours + neighbours[0:1]      # P2, P3, ... , P8, P9, P2
    char neighbours [] = {neighbours[0], neighbours[1]}
    count = 0
    return sum( (n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]) )  # (P2,P3), (P3,P4), ... , (P8,P9), (P9,P2)

def zhangSuen(image):
    "the Zhang-Suen Thinning Algorithm"
    Image_Thinned = image != 0  # deepcopy to protect the original image
    changing1 = changing2 = True        #  the points to be removed (set as 0)
    rows, columns = Image_Thinned.shape # x for rows, y for columns
    while changing1 or changing2:   #  iterates until no further changes occur in the image
        # Step 1
        changing1 = False

        for x in range(1, rows - 1):                     # No. of  rows
            for y in range(1, columns - 1):            # No. of columns
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                if (Image_Thinned[x][y] == 1     and    # Condition 0: Point P1 in the object regions
                    2 <= sum(n) <= 6   and    # Condition 1: 2<= N(P1) <= 6
                    transitions(n) == 1 and    # Condition 2: S(P1)=1
                    P2 * P4 * P6 == 0  and    # Condition 3
                    P4 * P6 * P8 == 0):         # Condition 4
                    Image_Thinned[x][y] = 0
                    changing1 = True
        # Step 2
        changing2 = False
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                if (Image_Thinned[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 6  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P2 * P4 * P8 == 0 and       # Condition 3
                    P2 * P6 * P8 == 0):            # Condition 4
                    Image_Thinned[x][y] = 0
                    changing2 = True

    return Image_Thinned
