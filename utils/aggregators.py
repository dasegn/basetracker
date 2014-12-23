from django.db.models import Aggregate
from django.db.models.sql.aggregates import Aggregate as SQLAggregate


class Concat(Aggregate):
    def add_to_query(self, query, alias, col, source, is_summary):
        aggregate = SQLConcat(col, source=source, is_summary=is_summary, **self.extra)
        query.aggregates[alias] = aggregate


class SQLConcat(SQLAggregate):
    sql_function = 'group_concat'

    @property
    def sql_template(self):
        separator = self.extra.get('separator')
        if separator:
            return '%(function)s(%(field)s, "%(separator)s")'
        else:
            return '%(function)s(%(field)s)'

class CompleteCountAggregate(SQLAggregate):
    is_ordinal = True
    sql_function = 'WEEK' # unused
    sql_template = "COUNT(CASE WHEN `bt_task`.`completed` = '1'  THEN `bt_task`.`id` ELSE null END)"

class CompleteCount(Aggregate):
    name = 'Complete'
    def add_to_query(self, query, alias, col, source, is_summary):
        query.aggregates[alias] = CompleteCountAggregate(col, source=source, is_summary=is_summary, **self.extra)