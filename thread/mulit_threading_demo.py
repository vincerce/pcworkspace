import time
import threading

__author__ = 'herexu'
__copyright__ = 'copyright 2017-2018'


def worker(n):
    print(f'{threading.current_thread().name} start at :{time.ctime()}')
    time.sleep(n)
    print('{} end at : {}'.format(threading.current_thread().name,time.ctime()))


def main():
    print('main satr at : <{}>'.format(time.ctime()))
    threads = []
    t1 = threading.Thread(target=worker , args=(4 ,))
    threads.append(t1)
    t2 = threading.Thread(target=worker , args=(2 ,))
    threads.append(t2)
    for t in threads:
        t.start()
    '''join thread make main wait'''
    for t in threads:
        t.join()
    print('main end at : <{}>'.format(time.ctime()))


if __name__ == '__main__':
    main()
