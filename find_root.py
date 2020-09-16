def approx_root(vector):
    """
    Returns the index of the values in 
    the given vector that are closest to the root
    """
    if min(vector) > 1e-5:
        return [np.argmin(np.abs(vector))]
    iroots = [
        i
        for i in range(1, len(vector)-2)
        if (0 > vector[i-1] and 0 < vector[i+1]) or (0 < vector[i-1] and 0 > vector[i+1])
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
    """
    fx = func(np.array(x)).tolist()
    #print(abs(fx[-1]))
    c = 0
    while abs(fx[-1]) > lim:
        x.append(x[-1] - fx[-1] * (x[-1] - x[-2]) / (fx[-1] - fx[-2]))
        fx.append(func(x[-1]))
        c += 1
        if c == 1000:
            print("no root found")
            return None
    return x[-1]
