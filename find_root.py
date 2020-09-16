import numpy as np

def approx_root(ar):
    """
    Returns the index of the values in 
    the given array ar that are closest to the root
    """
    if min(ar) > 1e-5:
        return [np.argmin(np.abs(ar))]
    iroots = [
        i
        for i in range(1, len(ar)-2)
        if (0 > ar[i-1] and 0 < ar[i+1]) or (0 < ar[i-1] and 0 > ar[i+1])
    ]
    roots = list()
    if len(iroots) > 1:
        for i in range(len(iroots)):
            try:
                if iroots[i+1] != iroots[i] + 1 and iroots[i+1] != iroots[i] - 1:
                    roots.append(iroots[i])
            except:
                roots.append(iroots[i])
    return roots

def sec_method(func, x, lim=1e-10):
    """
    Function that gets a root for the function
    that is passed, given 2 points, using the 
    secant method
    
    func is the function who's root its searching
    x is a list of two x values, preferably close to the root
    lim is how close to 0 you need it to be
    """
    fx = func(np.array(x)).tolist()

    c = 0
    while abs(fx[-1]) > lim:
        x.append(x[-1] - fx[-1] * (x[-1] - x[-2]) / (fx[-1] - fx[-2]))
        fx.append(func(x[-1]))
        c += 1
        if c == 1000:
            print("no root found")
            return None
    return x[-1]
