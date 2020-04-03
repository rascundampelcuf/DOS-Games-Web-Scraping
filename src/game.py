
class Game(object):
    
    def __init__(self):
        self.title = ''    
        self.category = ''
    
    def __str__(self):
        return 'Game({}, {})'.format(self.title, self.category)
    
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
        return [self.title, self.category]
