from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User
from django_enumfield import enum
from django.utils.encoding import python_2_unicode_compatible


class PriorityType(enum.Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    labels = {
        LOW: 'Low',
        MEDIUM: 'Medium',
        HIGH: 'High'
    }


@python_2_unicode_compatible
class Item(models.Model):
    title = models.CharField(max_length=140)
    created_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True, null=True, )
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User)
    priority = enum.EnumField(PriorityType, default=PriorityType.MEDIUM)
    note = models.TextField(blank=True, null=True)

    def overdue_status(self):
        if self.due_date and datetime.date.today() > self.due_date:
            return True
        else:
            return False

    def priority_label(self):
        if self.priority:
            return PriorityType.get(self.priority).label
        else:
            return ''


    def __str__(self):
        return self.title

    def save(self):
        if self.completed:
            self.completed_date = datetime.datetime.now()
        super(Item, self).save()

    class Meta:
        ordering = ["-due_date", "-priority"]

