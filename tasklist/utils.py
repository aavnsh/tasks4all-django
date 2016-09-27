import datetime

from django.contrib import messages

from tasklist.models import Item


def mark_done(request, done_items):
    for item in done_items:
        i = Item.objects.get(id=item)
        i.completed = True
        i.completed_date = datetime.datetime.now()
        i.save()
        messages.success(request, "Item \"{i}\" marked complete.".format(i=i.title))

def undo_completed_task(request, undone_items):
    for item in undone_items:
        i = Item.objects.get(id=item)
        i.completed = False
        i.save()
        messages.success(request, "Previously completed task \"{i}\" marked incomplete.".format(i=i.title))

