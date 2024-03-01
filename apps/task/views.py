from django.shortcuts import render, redirect
from apps.task.models import (
    Task,
    Status,
    Comment
)
from django.contrib.auth.models import User
from apps.task.forms import (
    CreateTask,
    TaskUpdateForm,

)
from django.shortcuts import (
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required


@login_required(login_url='router:user:login')
def home_page(request):
    task = Task.objects.all()
    context = {'tasks': task}
    return render(
        request=request,
        template_name='task/all_task.html',
        context=context
    )


@login_required(login_url='router:user:login')
def get_all_tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(
        request=request,
        template_name='task/all_task.html',
        context=context
    )


@login_required(login_url='router:user:login')
def create_new_task(request):
    statuses = Status.objects.all()
    creators = User.objects.all()

    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            product_data = form.cleaned_data
            Task.objects.create(**product_data)
            return redirect("router:tack:all-tasks")
        context = {
            'form': form,
            'statuses': statuses,
            'creators': creators
        }
    else:
        form = CreateTask()
        context = {
            'form': form,
            'statuses': statuses,
            'creators': creators
        }

    return render(
        request=request,
        template_name='task/create_task.html',
        context=context
    )


@login_required(login_url='router:user:login')
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    statuses = Status.objects.all()

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('router:task:all-tasks')

        context = {
            "form": form,
            "task": task,
            "statuses": statuses
        }
    else:
        form = TaskUpdateForm(instance=task)

        context = {
            "form": form,
            "task": task,
            "statuses": statuses
        }

    return render(
        request=request,
        template_name='task/update_task.html',
        context=context
    )


@login_required(login_url='router:user:login')
def get_task_info_by_task_id(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = Comment.objects.filter(
        task=task_id
    )

    context = {
        "task": task,
        "comments": comments
    }
    #####
    return render(
        request=request,
        template_name='task/task_info.html',
        context=context
    )


@login_required(login_url='login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.delete()
    return redirect('router:task:all-tasks')


@login_required(login_url='login')
def get_comment_info(request):
    comments = Comment.objects.filter(
        creator=request.user
    )

    context = {
        "comments": comments
    }

    return render(
        request=request,
        template_name='task/all_comment.html',
        context=context
    )


@login_required(login_url='login')
def get_comment_info_by_id(request, comment_id):
    comments = get_object_or_404(Comment, id=comment_id)

    context = {
        "comments": comments
    }

    return render(
        request=request,
        template_name='task/comment_info.html',
        context=context
    )


@login_required(login_url='login')
def create_comment(request):
    task_id = request.GET.get("task_id")

    user = get_object_or_404(User, id=request.user.id)
    statuses = Status.objects.all()
    task = get_object_or_404(Task, id=task_id)

    form = CommentCreateForm()

    if request.method == 'POST':
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('task-info', task_id=task_id)

    context = {
        "form": form,
        "user": user,
        "statuses": statuses,
        "task": task
    }

    return render(
        request=request,
        template_name='task/create_comment.html',
        context=context
    )


@login_required(login_url='login')
def update_comment(request, comment_id):
    comments = get_object_or_404(Comment, id=comment_id)

    form = CommentUpdateForm(instance=comments)

    if request.method == 'POST':
        form = CommentUpdateForm(request.POST, instance=comments)

        if form.is_valid():
            form.save()

            return redirect('all-comment')

    context = {
        "form": form,
        "comments": comments,
    }

    return render(
        request=request,
        template_name='task/update_comment.html',
        context=context
    )


@login_required(login_url='login')
def delete_comment(request, comment_id):
    subtask = get_object_or_404(Comment, id=comment_id)

    subtask.delete()
    return redirect('all-comment')




