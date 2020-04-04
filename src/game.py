
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
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
          
    @property
    def violence(self):
        return self._violence
    
    @violence.setter
    def violence(self, violence):
        self._violence = violence
        
        
    def get_category(self):
        return self.category
    
    def set_category(self, value):
        self.category = value
        
    def get_list(self):
        return [self._title, self._category]
