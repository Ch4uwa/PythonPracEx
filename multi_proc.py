from multiprocessing import Process, Pipe
import multiprocessing
import logging

logger = multiprocessing.log_to_stderr()
logger.setLevel(logging.INFO)


def display(my_name):
    print('Hi !! I am Python', my_name)


def cube(n):
    for x in n:
        print(f'{x} cube is {x**3}')


def even_nr(n, q=None):
    for x in n:
        if x % 2 == 0:
            print(f'{x} is an even number ')
            if q is not None:
                q.put(x)


def myfunction(conn):
    conn.send(['hi!! I am Python, and im a child'])
    conn.close()


if __name__ == '__main__':
    my_numbers = [3, 4, 5, 6, 7, 8]
    q = multiprocessing.Queue()
    parent_conn, child_conn = Pipe()
    p1 = Process(target=display, args=('Martin',))
    p2 = Process(target=cube, args=(my_numbers,))
    p3 = Process(target=even_nr, args=(my_numbers,))
    p4 = Process(target=myfunction, args=(child_conn,))
    p5 = Process(target=even_nr, args=(range(10), q))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    print(parent_conn.recv())
    while not q.empty():
        print(q.get())

    print('DONE')
