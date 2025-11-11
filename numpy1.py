""" Understanding Data Types in Python"""

# import numpy as np

# result = 0
# for i in range(100):
#     result += i
#     print(result)


# x = 4 
# print(x)
# x = "four"
# print(x)

# ------------------ A Python Integer Is More Than Just an Integer ----------------- #

x = 10000 # ---> python

# /* C
""" struct _longobject {
 long ob_refcnt;
 PyTypeObject *ob_type;
 size_t ob_size;
 long ob_digit[1];
}; """


# -------------------- A Python List Is More Than Just a List ---------------------- #

# L = list(range(10)) # tip -----> int 
# print(L)
# print(type(L[0]))

# print()

# L2 = [str(c) for c in L] # tip -----> str
# print(L2)
# print(type(L2[0]))

# print()

# L3 = [True, "2", 3.0, 4] # tip -----> mixed types
# print([type(item) for item in L3]) 





# ----------------------- Fixed-Type Arrays in Python ------------------------------ #

# import array
# L = list(range(10))
# A = array.array("i", L)
# print(A)
# print(type(L))



# ----------------------- Creating Arrays from Python Lists ------------------------ #

# import numpy as np

# x = np.array([1, 4, 2, 5, 3])
# print(x)

# print()

# x = np.array([3.14, 4, 2, 3])
# print(x)

# print()

# x = np.array([1, 2, 3, 4], dtype= "float32") # massivni aniq turini bilmoqchi bolsak dtype= func fodalanish kerak.
# print(x)



# x = np.array([range(i, i + 3) for i in [2, 4, 6]])
# print(x)


# ------------------------- Creating Arrays from Scratch --------------------------- #

import numpy as np


# m = np.zeros(10, dtype= int)
# print(m)


# m = np.ones((3, 5), dtype= float)
# print(m)

# m = np.full((3, 5), 3.14)
# print(m)


""" Ketma-ketlik va random qiymatlar bilan massiv yaratish"""

# x = np.arange(0, 20, 2)
# print(x)


# x = np.linspace(0, 1, 5)
# print(x)


# x = np.random.random((3, 3))
# print(x)


""" Tasodifiy (random) massivlar """


# x = np.random.normal(0, 1, (3, 3))
# print(x)



# x = np.random.random((3, 3))
# print(x)


# x = np.random.normal(0, 1, (3, 3))
# print(x)


# x = np.random.randint(0, 10, (3, 3))
# print(x)



""" Maxsus tuzilmalar """

# x = np.eye(3)
# print(x)


# x = np.empty(3)
# print(x)