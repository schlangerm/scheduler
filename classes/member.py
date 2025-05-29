from schedule import Schedule

#This is a very light concept at the moment
class Member: 
    def __init__(self, name):
        self.name = name

    def set_schedule(self, schedule: Schedule):
        self.schedule = schedule

    def get_schedule(self):
        return self.schedule
    
    