
class Game(object):
    
    def __init__(self, title, violence, category, year):
        self._title = title
        self._violence = violence
        self._category = category
        self._year = year
    
    def __str__(self):
        return 'Game({}, {}, {}, {})'.format(self._title, self._violence, self._category, self._year)
    
    def __repr__(self):
        return str(self)
        
    def get_list(self):
        return [self._title, self._category, self._year, self._violence]
