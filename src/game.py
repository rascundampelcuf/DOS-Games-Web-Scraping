
class Game(object):
    
    def __init__(self):
        self._title = ''
        self._category = ''
        self._year = ''
        self._violence = ''
    
    def __str__(self):
        return 'Game({}, {})'.format(self._title, self._violence)
    
    def __repr__(self):
        return str(self)
    
    def get_title(self):
        return self.title
    
    def set_title(self, value):
        self.title = value
        
    def get_category(self):
        return self.category
    
    def set_category(self, value):
        self.category = value
        
    def get_list(self):
        return [self._title, self._category]
