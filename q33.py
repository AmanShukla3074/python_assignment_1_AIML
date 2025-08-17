# 33. Remove all punctuation marks from a string.

import string
s = "Hello, World! Python is great language."
result = "".join(ch for ch in s if ch not in string.punctuation)
print(result)