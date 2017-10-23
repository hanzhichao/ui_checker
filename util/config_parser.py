from base.data_file_parser import ConfFile


class Config(object):
    def __init__(self):
        pass
    PATH = '../conf/default.conf'
    _dict = ConfFile.load(PATH)
    try:
        base_url = _dict['env']['base_url']
        wait = _dict['env']['wait']
        sleep = _dict['env']['sleep']
        username = _dict['login']['username']
        password = _dict['login']['password']
    except Exception,e:
        raise Exception,e

    @property
    def get(cls, section, option):
        try:
            return _dict[section][option]
        except Exception,e:
            raise Exception,e


class PageElm(object):
    def __init__(self, path):
        self.path = path
    _dict = ConfFile.load(self.path)
    
    try:
        menu = _dict['page']['menu']
        subject = _dict['page']['subject']
    except Exception,e:
        raise Exception,e

    @property
    def get(option):
        try:
            return _dict['element'][option]
        except Exception,e:
            raise Exception,e
