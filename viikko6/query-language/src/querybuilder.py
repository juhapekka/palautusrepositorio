from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder():
    def __init__(self, matcher=And()):
        self._matcher = matcher

    def plays_in(self, team):
        return QueryBuilder(And(PlaysIn(team), self._matcher))
    
    def has_at_least(self, number, attr):
        return QueryBuilder(And(HasAtLeast(number, attr), self._matcher))

    def has_fewer_than(self, number, attr):
        return QueryBuilder(And(HasFewerThan(number, attr), self._matcher))

    def not_(self):
        return QueryBuilder(Not(self._matcher))

    def all(self):
        return QueryBuilder(All(self._matcher))
    
    def or_(self):
        return QueryBuilder(Or(self._matcher))
        
    def build(self):
        return self._matcher