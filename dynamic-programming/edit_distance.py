from __future__ import print_function


class EditDistance:

    def __init__(self):
        self.__prepare__()

    def __prepare__(self, N = 0, M = 0):
        self.dp = [[-1 for y in range(0,M)] for x in range(0,N)]

    def __solveDP(self, x, y):
        if (x==-1):
            return y+1
        elif (y==-1):
            return x+1
        elif (self.dp[x][y]>-1):
            return self.dp[x][y]
        else:
            if (self.A[x]==self.B[y]):
                self.dp[x][y] = self.__solveDP(x-1,y-1)
            else:
                self.dp[x][y] = 1+min(self.__solveDP(x,y-1), self.__solveDP(x-1,y), self.__solveDP(x-1,y-1))

            return self.dp[x][y]

    def solve(self, A, B):
        if isinstance(A,bytes):
            A = A.decode('ascii')

        if isinstance(B,bytes):
            B = B.decode('ascii')

        self.A = str(A)
        self.B = str(B)

        self.__prepare__(len(A), len(B))

        return self.__solveDP(len(A)-1, len(B)-1)
