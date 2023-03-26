from django.utils.timezone import now, timedelta
class CheckAgeMixin:

    def is_older_than(self, days=1):
        delta = timedelta(days=days)
        return (now() - self.created) > delta


class LastModifiedMixin:

    def is_modified_in_last(self, minutes=15):
        """Czy modyfikowany w ciągu ostatnich minutes"""
        delta = timedelta(minutes=minutes)
        return (now() - self.modified) < delta

