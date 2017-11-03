import time
import inspect


def show_duration(action):
    def wrapper(*args, **kwargs):
        start = time.time()
        end = time.time()
        duration = end - start
        parent_action = inspect.stack()[1][4][0].strip()
        # inspect.getargspec(action)
        # varnames = action.__code__.co_varnames
        print '%s---%s---%ss' % (parent_action, action.__name__, duration)
        return action(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    pass

