from data import ConfFile

def conf(section, option):
    path = '../conf/default.conf'
    return ConfFile.get(path,section,option)

def page(filename):
    path = '../conf/page_elm/' + filename + '.ini'
    _page = ConfFile.load_section(path,'page')
    _page['menu']=tuple(_page['menu'].split(','))
    return _page


def elm(filename, element):
    path = '../conf/page_elm/' + filename + '.ini'
    return tuple(ConfFile.get(path,'element',option).split(','))

# class Config(object):
#     def __init__(self):
#         pass
#     PATH = '../conf/default.conf'
#     _dict = ConfFile.load(PATH)
#     try:
#         base_url = _dict['env']['base_url']
#         wait = _dict['env']['wait']
#         sleep = _dict['env']['sleep']
#         username = _dict['login']['username']
#         password = _dict['login']['password']
#     except Exception,e:
#         raise Exception,e

#     @property
#     def get(cls, section, option):
#         try:
#             return _dict[section][option]
#         except Exception,e:
#             raise Exception,e
#     def check():
#         pass

# class PageElm(object):
#     def __init__(self, path):
#         self.path = path
#         self._dict = ConfFile.load(path)
        
#         try:
#             self.menu =tuple(self._dict['page']['menu'].split(',')) 
#             self.subject = self._dict['page']['subject']
#         except Exception,e:
#             raise Exception,e

#     @property
#     def get(option):
#         try:
#             return tuple(_dict['element'][option].split(','))
#         except Exception,e:
#             raise Exception,e
    
#     def check():
#         pass

