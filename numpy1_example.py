import numpy as np
""" 🧠 1. Understanding Data Types in Python """

# m1

# a = 10
# b = 3.5
# c = "AI"
# d = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# m2

# x = 5 
# y = "5"
# try:
#     print(x + y)
# except TypeError:
#     print(f"int va str tipini qoshib bolmaydi.")



# m3

# mixs = [1, "hello", 3.14, True]
# for j in mixs:
#     print(f"Type: {type(j)}")


# m4

# x = 3.8
# y = "10"
# try:
#     c = int(x) + float(y)
#     print(f"Summa: {c}")
# except TypeError:
#     print(" You can't add a number and a string together. ")


# m5

# x_int = 0
# y_int = 1
# s_str = "AI"
# s_tuple = ""
# l_list = []

# mixs_list = [x_int, y_int, s_str, s_tuple, l_list]
# for mixs in mixs_list:
#     print(f"Situation:{bool(mixs)}")





""" ⚙️ 2. Introduction to NumPy """


# m1

# import numpy as np
# print(np.__version__)



# m2

# array = np.array([1, 2, 3, 4, 5, 6])
# print(array)


# m3
# x = np.arange(0, 10, 2)
# print(x)


# m4

# x = np.zeros(5)
# y = np.ones(5)
# print(x, "\n", y)


#  m5

# x = np.random.randint(1, 10, size= 5)
# print(x)



""" 🧩 3. Fixed-Type Arrays in Python """


import array

# x = array.array("i", [1, 2, 3, 4, 5])
# print(x)


# x = array.array("i", [1, 2, 3, 4, 5, 6])
# x.append(5)
# print(x)

""" x = array.array("i", [1, 2, 3, 4, 5])
x = 
print() """


# x = np.array([1, 2, 3, 4, 5], dtype= "int32")
# print(x)

""" list = ([1, 2, 3, 4], )
x = np.array(([1, 2, 3, 4]), )
print(list) """



""" 🔢 4. Creating Arrays in NumPy """

# x = np.array([[1, 2, 3], [4, 5, 6]])
# print(x)


# zeros = np.zeros((3, 3))
# ones = np.ones((2, 4))
# print(zeros)
# print()
# print(ones)
# print()



# x = np.arange(1, 11)
# y = np.linspace(0, 1, 5)
# print(x)
# print(y)


# full = np.full((3, 3), 1.74)
# print(full)

# x = np.random.randint(0, 100, (3, 3))
# y = np.eye(4)
# print(y)
# print(x) 