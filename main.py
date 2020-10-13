import numpy as np
from hill_cypher import encode, decode

# key = np.array([[9, 4], [5, 7]])
key = np.array([[1, 3, -1], [6, 1, 1], [-5, 4, -3]])
# key = np.array([[6, 1, 3, 5], [2, 9, 0, 9], [8, 0, 1, 9], [7, 8, 0, 8]])
# key = np.round(np.random.rand(10, 10) * 10) # Key can be invalid

toEncode = "The quick brown fox jumps over the lazy dog"

print("Encoding:", toEncode)
encoded = encode(toEncode, key)
print("Encoded: ", encoded)
print("Decoded: ", decode(encoded, key))