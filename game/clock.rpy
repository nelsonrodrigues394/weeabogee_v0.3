init python:
    class Clock(object):
        def __init__(self, hour=0, minute=0):
            self.hour = hour
            self.minute = minute
        
        @property
        def string(self):
            if self.hour >= 0 and self.hour <= 9:
                if self.minute == 0:
                    return "0%d:0%d"%(self.hour, self.minute)
                else:
                    return "0%d:%d"%(self.hour, self.minute)
            else:
                if self.minute == 0:
                    return "%d:0%d"%(self.hour, self.minute)
                else:
                    return "%d:%d"%(self.hour, self.minute)
        
        def jobHour(self):
            self.hour += 6
        
        def dayHour(self):
            self.hour = 6
            self.minute = 0
        
        def next(self, minute = 1):
            while minute:
                minute -= 1
                if self.minute == 30:
                    self.minute = 0
                    if self.hour == 23:
                        self.hour = 0
                    else:
                        self.hour += 1
                else:
                    self.minute += 30
                
        