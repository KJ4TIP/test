def c(*funs):
    """Compose a list of functions"""
    
    return reduce(lambda g, f: lambda x: f(g(x)), reversed(funs))

def curry(f, n):
    """Transform function f into a curried function of arity n"""

    helpmsg = "A curried version of the following function, arity {}.\n\n"
    def _curry(f, n, oargs):
        def __curry(*args):
            targs = oargs + list(args)
            if len(targs) >= n:
                return f(*targs)
            else:
                return _curry(f, n, targs)
            
        return __curry
    g = _curry(f, n, [])
    if f.__doc__ is not None:
        g.__doc__ = helpmsg.format(n) + f.__doc__
    return g

def curry_n(n):
    """Create a function decorator to curry a function with arity n
    
    Intended use:
    @functional.curry_n(2)
    def blah(spam, eggs):
        ...
    """
    return lambda f: curry(f, n)

def scanl(f, a, xs):
    result = [a]
    for x in xs:
        a = f(a, x)
        result.append(a)
    return result

def scanl1(f, xs):
    a = xs[0]
    return scanl(f, a, xs[1:])

def swap(f):
    return curry(lambda x, y: f(y, x), 2)

@curry_n(4)
def ifelse(p, f, g, x):
    if p(x):
        return f(x)
    else:
        return g(x)

@curry_n(2)
def cnst(x, *unused):
    return x

id = lambda x: x

cmap = curry(map, 2)
creduce = curry(lambda f, i, l: reduce(f, l, i), 3)

attr = curry(lambda key, d: d[key], 2)
lt = curry(lambda a, b: a > b, 2)
gt = curry(lambda a, b: a < b, 2)
eq = curry(lambda a, b: a == b, 2)
ne = curry(lambda a, b: a != b, 2)

plus = curry(lambda a, b: a + b, 2)
