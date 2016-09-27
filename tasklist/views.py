import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from tasklist.forms import AddItemForm, EditItemForm
from tasklist.models import Item
from tasklist.utils import mark_done, undo_completed_task

@login_required()
def view_list(request, filter_type='mine', view_completed=False):

    mark_done(request, request.POST.getlist('mark_done'))
    undo_completed_task(request, request.POST.getlist('undo_completed_task'))

    thedate = datetime.datetime.now()
    created_date = "%s-%s-%s" % (thedate.year, thedate.month, thedate.day)

    if filter_type == "mine":
        task_list = Item.objects.filter(created_by=request.user, completed=False).order_by('due_date', '-priority')
        completed_list = Item.objects.filter(created_by=request.user, completed=True).order_by('due_date', '-priority')
    elif filter_type == "recent-add":
        task_list = Item.objects.filter(
            created_by=request.user,
            completed=False).order_by('-created_date')[:50]
    elif filter_type == "recent-complete":
        task_list = Item.objects.filter(
            created_by=request.user,
            completed=True).order_by('-completed_date')[:50]
    else:
        task_list = Item.objects.filter(created_by=request.user, completed=False).order_by('due_date', '-priority')
        completed_list = Item.objects.filter(created_by=request.user, completed=True).order_by('due_date', '-priority')

    if request.POST.getlist('add_task'):
        form = AddItemForm(request.POST, initial={
            'created_by': request.user.id
        })

        if form.is_valid():
            new_task = form.save()

            messages.success(request, "New task \"{t}\" has been added.".format(t=new_task.title))
            return HttpResponseRedirect(request.path)
    else:
        if filter_type != "mine" and filter_type != "recent-add" and filter_type != "recent-complete":
            form = AddItemForm(initial={
                'created_by': request.user.id,
            })

    return render(request, 'tasklist/view_list.html', locals())

@login_required()
def view_task(request, task_id):
    task = get_object_or_404(Item, pk=task_id)

    if task.created_by == request.user:
        if request.POST:
            form = EditItemForm(request.POST, instance=task)

            if form.is_valid():
                form.save()
                messages.success(request, "The task has been edited.")

                return HttpResponseRedirect(reverse('incomplete_tasks'))
        else:
            form = EditItemForm(instance=task)
            if task.due_date:
                thedate = task.due_date
            else:
                thedate = datetime.datetime.now()
    else:
        messages.info(request, "You do not have permission to view/edit this task.")

    return render(request, 'tasklist/view_task.html', locals())

