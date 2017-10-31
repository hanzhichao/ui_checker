import time


def show_duration(action):
    def wrapper(*args, **kwargs):
        start = time.time()
        action(*args, **kwargs)
        end = time.time()
        s = end - start
        print '%ss' % s
        return action
    return wrapper
