from joblib import Parallel, delayed
import time

def f(i):
    time.sleep(i**2 / 100)
    return i**2


print([1, 2] == [2, 1])
n = 20
actual = Parallel(n_jobs=3, verbose=100)(delayed(f)(i) for i in range(n))
expect = [i**2 for i in range(n)]
print(actual == expect)
