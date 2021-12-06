import string
ALLOWED = frozenset(string.ascii_letters + string.digits + '_' + '-')

def check(mystring):
    return all(c in ALLOWED for c in mystring)

print(check('764839w6@'))