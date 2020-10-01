# Question: Filter the dictionary by removing all items with a value of
# greater than 1.
# d = {"a": 1, "b": 2, "c": 3}
# Expected output:  {'a': 1}

d = {"a": 1, "b": 2, "c": 3}

d1 = {k: v for k, v in d.items() if d[k] <= 1}
print(d1)


# Use dictionary comprehension.
# Inside the dictionary comprehension access dictionary items with d.items()
# if you are on Python 3, or dict.iteritems()  if you are on Python 2.
