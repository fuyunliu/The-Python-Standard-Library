
from http import cookies


HTTP_COOKIE = '; '.join([
    r'integer=5',
    r'string_with_quotes="He said, \"Hello, World!\""',
])


print('From constructor:')
c = cookies.SimpleCookie(HTTP_COOKIE)
print(c)

print()
print('From load():')
c = cookies.SimpleCookie()
c.load(HTTP_COOKIE)
print(c)
