init python:
    
    class Calendar(object):
        def __init__(self, day=1, month=1, year=1):
            self.day = day
            self._month = month - 1
            self.year = year
           
            self.daycount_from_gamestart = 0
           
            self.days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
            self.month_names = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                                               'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
            self.days_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        @property    
        def game_day(self):
            return self.daycount_from_gamestart + 1
        
        @property    
        def game_week(self):
            weekidx = self.daycount_from_gamestart / len(self.days)
            return weekidx + 1

        @property    
        def weekday(self):
            daylistidx = self.daycount_from_gamestart % len(self.days)
            return self.days[daylistidx]
            
        @property
        def month_number(self):
            return self._month + 1
            
        @property
        def month(self):
            return self.month_names[self._month]
    
        @property
        def last_day_of_the_month(self):
                return self.day == self.days_count[self._month]
            
        @property        
        def string(self):
            return "%d de %s de %d - %s"%(self.day, self.month, self.year, self.weekday)
        
        def next(self, days=1):
            self.daycount_from_gamestart += days
            while days:
                self.day += 1
                days -= 1
                if self.day > self.days_count[self._month]:
                    self._month += 1
                    self.day = 1
                    if self._month > 11:
                        self._month = 0
                        self.year += 1
