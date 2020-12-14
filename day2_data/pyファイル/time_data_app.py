from dataaccess import DataAccess
import itertools

hoge = DataAccess()
x = list(itertools.chain.from_iterable(hoge.get_spots()))
x.insert(0,"when_build:")
print(x)
