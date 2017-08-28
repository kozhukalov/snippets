import multiprocessing
import time
import signal
import logging
import sys

logging.basicConfig(stream=sys.stderr)


def worker_init(q, worker_lamda):
    # ignore the SIGINI in sub process, just print a log
    def sig_int(signal_num, _):
        logging.info('signal is caught: %s', signal_num)
    signal.signal(signal.SIGINT, sig_int)

    print("Worker init")
    while True:
        item = q.get()

        if item is None:
            break

        worker_lamda(item)
        q.task_done()


def main():
    def worker_lambda(s):
        time.sleep(1)
        print(s)

    q = multiprocessing.JoinableQueue()
    pool = multiprocessing.Pool(processes=4, initializer=worker_init, initargs=(q, worker_lambda))

    try:
        for i in range(100):
            print("Put: {}".format(i))
            q.put(i)
        q.join()

        print("Tasks are done")
        for _ in range(4):
            q.put(None)

        pool.close()
        pool.join()
    except KeyboardInterrupt:
        pool.terminate()
        pool.join()


if __name__ == "__main__":
    main()