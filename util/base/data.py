from ConfigParser import ConfigParser

class Conf(object):
    """docstring for Conf"""
    
    @classmethod
    def _open(cls, path):
        try:
            return open(path)
        except IOError as e:
            print "%s not exist!Open file fail!" % path
            raise IOError, "%s not exist!Open file fail!" % path

    @classmethod
    def load(cls, path):
        cf = ConfigParser()
        try:
            cf.read(path)
        except IOError as e:
            raise IOError,e

        cf_dict = {}
        print cf.sections()
        print cf.options('env')
        print cf.items('db')
        # for section in cf.sections():
        #     for option in cf.options(section):
        #         cf_dict['section']['option'] = cf.items['option']

        print cf_dict






if __name__ == '__main__':
    Conf.load('../../conf/default.conf')


