# Hill Cipher algorithm 

This is a polygraphic substitution cipher based on linear algebra. 

It can encode and decode a string using matrices manipulation. 

This algorithm allows for any dimension matrix key.

Tested in Python 3.7.


## Example 

```key = np.array([[9, 4], [5, 7]])
toEncode = "HELLOWORLD"

encoded = encode(toEncode, key)
print(encoded) # "NWZNSBYSTJ"

print(decode(encoded, key)) # "HELLOWORLD"
```

## Resources used 
https://www.apprendre-en-ligne.net/auteur/articles/Hill.pdf (fr) 

https://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/Python-matrices.pdf (fr)

https://en.wikipedia.org/wiki/Hill_cipher