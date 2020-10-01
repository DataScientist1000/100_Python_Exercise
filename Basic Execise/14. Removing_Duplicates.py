# Question: Complete the script so that it removes duplicate items from list a.

# a = ["1", 1, "1", 2]
# Expected output: ['1', 2, 1]

# ------------
from collections import OrderedDict
a = ["1", 1, "1", 2]
print(list(set(a)))

# Hint 1: Sets are datatypes where duplicates are not allowed.
# Hint 2: You can use a set function to convert the list to a set and then a
#  list function to convert the set back to a list.

# We used a set  function to convert the list to a set which would
#  intermediately produce {'1', 1, 2}  with no duplicates because set objects
# cannot contain duplicates. Then using list  we converted the set back to a list.
# The drawback here is that the original order of the items is lost.
# If you need to preserve the order you may want to use the solution in Answer 2 below.

# Answer 2:

b = ["1", 1, "1", 2]
b = list(OrderedDict.fromkeys(b))
print(b)

# Explanation 2:
# Ordered dictionaries are another data type in Python that unlike sets and
#  normal dictionaries they preserve the order of the items.
#  Here OrderedDict.fromkeys(a)  would produce an OrderedDict
# like [('1', None), (1, None), (2, None)] .
# Then we would convert that OrderedDict  to a list.

# Answer 3:

a1 = ["1", 1, "1", 2]
b1 = []
for i in a1:
    if i not in b1:
        b1.append(i)

print(b1)
# Explanation 3:

# This is another solution that would preserve the original order.
# We go through all items of the original list and append them to
# the new list if they have not been appended before. The downside of
# this is the operation can take a lot of time if the list is large as
# we need to access both lists and also perform a conditional in each iteration.
