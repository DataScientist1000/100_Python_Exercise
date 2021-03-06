# Question: Calculate the sum of the values of keys a  and b .

# d = {"a": 1, "b": 2, "c": 3}
# Expected output: 3

d = {"a": 1, "b": 2, "c": 3}

# for i in d.values():
#     print(i)


print((d["a"] + d["b"]))
# print(sum(d["a"].value() , d["b"]).value())

# It's as easy as that. However, if you want to do the sum of all dictionary
#  values you need to take another approach instead of accessing
# all values one by one.
# We're going through that approach later on in another exercise.
