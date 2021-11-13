# Source : https://leetcode.com/problems/determine-color-of-a-chessboard-square/
# Author : foxfromworld
# Date  : 13/11/2021
# Second attempt

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in 'bdfh' and int(coordinates[1]) % 2 == 0:
            return False
        elif coordinates[0] in 'aceg' and int(coordinates[1]) % 2 != 0:
            return False
        else:
            return True    

# Date  : 13/11/2021
# First attempt

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        if x[coordinates[0]] % 2 == 0 and int(coordinates[1]) % 2 == 0:
            return False
        elif x[coordinates[0]] % 2 != 0 and int(coordinates[1]) % 2 != 0:
            return False
        else:
            return True
