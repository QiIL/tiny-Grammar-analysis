from tiny_analisis import TINY_PROGRAME

articleCon = 'x = 1;\n b = 2; EOF'


def getToken():
    for token in TINY_PROGRAME.findall(articleCon):
        yield token


token_generator = getToken()  # 

def nextToken():
    try:
        token = next(token_generator)
        return token
    except StopIteration:
        return False

while nextToken():
    print nextToken()

'''
def a():
    for i in range(10):
        yield i

try:
    token = next(a())
    print token
except StopIteration:
    print False

try:
    token = next(a())
    print token
except StopIteration:
    print False'''