# In matrix we define any collection inside another collection.
# It can be a*b, a*b*c and so on
_mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
print(_mat[0])
print(_mat[1])
print(_mat[2])

# Transpose of a matrix covered in list comprehension
_mat = [[_mat[inc][j] for inc in [i for i in range(len(_mat))]] for j in range(4)]
print(_mat)