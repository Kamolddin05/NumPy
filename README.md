# NumPy    Python Data Science Handbook
NumPy is a Python library for working with data quickly and easily. It mainly works with multi-dimensional arrays and makes calculations very fast.

Main points:

ndarray — multi-dimensional array.

Vectorization — apply operations to arrays at once.

Broadcasting — handle arrays with different shapes automatically.

Creating arrays:

np.array([1,2,3]) — from a list.

np.zeros() / np.ones() — arrays of 0s or 1s.

np.arange() / np.linspace() — sequences of numbers.

Indexing and slicing:

Simple: x[0], x[-1]

Slice: x[1:5], x[:3], x[::2]

2D array: X[0,1], X[:,1], X[1,:]

Math operations:

+, -, *, /

Statistics: np.mean(), np.sum(), np.std()

Matrix: np.dot(), x.T, np.linalg.inv()

Useful features:

Boolean indexing: x[x>0]

Fancy indexing: x[[1,3,5]]

Summary:
NumPy is fast, convenient, and efficient. It is a key tool in Data Science and Machine Learning projects.
