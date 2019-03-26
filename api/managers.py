from django.db import models


class TownQuerySet(models.query.QuerySet):
    def count_towns(self, dept_code):
        """
        Count the number of towns by filtering on dept_code. In SQL, it means :
        SELECT dept_code, COUNT(code)
        FROM api_town WHERE dept_code=1;
        > 1|410
        """
        return {
            'count': len(self.filter(dept_code=dept_code)),
        }

    def calculate_aggregates(self, **kwargs):
        if 'count_towns' in kwargs:
            if kwargs['count_towns'] == 'dept':
                return self.count_towns(kwargs['dept_code'])


class TownManager(models.Manager):
    def get_queryset(self):
        """Overrides get_queryset method and loads the custom TownQuerySet"""
        return TownQuerySet(self.model, using=self._db)

    def calculate_aggregates(self):
        return self.get_queryset().calculate_aggregates()
