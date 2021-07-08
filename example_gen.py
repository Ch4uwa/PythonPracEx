# ex_gen.py


def generator_thr_iter():
    yield 42
    yield 34.2
    yield 'This is a string'


def num_gen(n):
    num = 1
    while True:
        yield num
        if num == n:
            return
        else:
            num += 1


for i in num_gen(200000):
    print(i*i)

g_iter = generator_thr_iter()
for i in g_iter:
    print(1, i)

# print(g_iter.__next__())
# print(g_iter.__next__())
# print(g_iter.__next__())
