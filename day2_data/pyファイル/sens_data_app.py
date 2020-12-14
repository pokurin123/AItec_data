from dataaccess import DataAccess
import itertools

hoge = DataAccess()
count = 0
x = list(itertools.chain.from_iterable(hoge.get_spots()))
for i in ["spot_type:","rating_5Lv:","history:","culture:","nature:","religion:","amusement:"]:
    print(i,x[count])
    count += 1
