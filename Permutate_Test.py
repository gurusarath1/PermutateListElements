import Permutate


#Example1
x = Permutate.generate_permutation_List([1,2,3])
print(x)

#Example2
listX = ['A',2,3,'C']
Permutate.generate_permutation_List(listX, printOutput = True, stringFormatOutput = True)


"""
OUTPUT ----
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
A23C
A2C3
A32C
A3C2
AC23
AC32
2A3C
2AC3
23AC
23CA
2CA3
2C3A
3A2C
3AC2
32AC
32CA
3CA2
3C2A
CA23
CA32
C2A3
C23A
C3A2
C32A
[Finished in 0.1s]
"""