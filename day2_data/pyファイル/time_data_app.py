from pre_dataaccess import DataAccess
import itertools

for id_n in list(range(1,10)):
    hoge = DataAccess()
    x = list(itertools.chain.from_iterable(hoge.get_spots(id_n)))
    x.insert(2,"close")
    x.insert(1,"open")
    x.insert(0,"when_build")

    print(x)
