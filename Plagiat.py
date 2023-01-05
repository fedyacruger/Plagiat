import argparse
import numpy as np
import ast

class Compare:
    
    def __init__(self):
        self.output = []
        self.L = []
        
        parser = argparse.ArgumentParser(description='compare')
        parser.add_argument('input', type = str, help='Input')
        parser.add_argument('output', type=str, help='Output path')
        args = parser.parse_args()
        
        with open(args.input, "r") as f:
            for line in f:
                self.L.append(line.split() )
        
        self.output = args.output
        
    def Levi_dist(self, s1, s2):
        M = len(s1)
        N = len(s2)
        D = np.zeros((M + 1, N + 1))
        D[0][0] = 0
        for i in range(1, M + 1):
            D[i][0] = i

        for j in range(1, N + 1):
            D[0][j] = j

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                a = D[i][j - 1] + 1
                b = D[i - 1][j] + 1
                m = 0
                if s1[i - 1] == s2[j - 1]:
                    m = 0
                else:
                    m = 1
                c = D[i - 1][j - 1] + m

                D[i][j] = min(a, b, c)
        print(D[M][N])
        return D[M][N]/max(len(s1), len(s2))
    
    def Result(self):
        distances = []
        
        for i in range(len(self.L)):
            f1 = open(self.L[i][0], "r")
            f2 = open(self.L[i][1], "r")
            t1 = ast.parse(f1.read())
            t2 = ast.parse(f2.read())
            s1 = ast.dump(t1, annotate_fields = False)
            s2 = ast.dump(t2, annotate_fields = False)
            distances.append(self.Levi_dist(s1, s2))
            print("OK")
            f1.close()
            f2.close()
            
            
        with open(self.output, "w") as G:
            for  d in distances:
                G.write(str(1-d) + '\n')
    

c = Compare()
c.Result()
