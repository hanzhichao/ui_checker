from file import ConfFile
from util import project_root


def get_all():
    path = project_root() + '/conf/default.conf'
    return ConfFile.load(path)


def get_section(section):
    path = project_root() + '/conf/default.conf'
    return ConfFile.load_section(path, section)


def get(section, option):
    path = project_root() + '/conf/default.conf'
    return ConfFile.get(path, section, option)


class Config(object):
    def __init__(self, path='../conf/default.conf'):
        self.path = path
        self._dict = ConfFile.load(path)

    def config(self):
        return self._dict

    def section(self, section):
        try:
            return self._dict[section]
        except KeyError:
            raise KeyError, "No section '%s' in '%s'" % (section, self.path)

    def get(self, section, option):
        section_dict = self.section(section)
        try:
            return section_dict[option]
        except KeyError, e:
            raise KeyError, "No option '%s' in section '%s' of '%s'" % (option, section, self.path)


if __name__ == '__main__':
    conf = Config()
    print conf.get('email', 'smtp_server')
