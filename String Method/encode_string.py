# UTF-8 encode the string:

txt = "My name is Ståle"

x = txt.encode()

print(x)

txt = "My name is Ståle"

# Various encoding

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
