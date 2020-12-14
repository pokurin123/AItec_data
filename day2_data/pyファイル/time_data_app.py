from dataaccess import DataAccess
import itertools

hoge = DataAccess()
count = 0
x = list(itertools.chain.from_iterable(hoge.get_spots()))
for i in ["when_build:","open:","close:"]:
    print(i,x[count])
    count += 1
