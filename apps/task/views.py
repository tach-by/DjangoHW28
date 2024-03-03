from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from apps.task.models import (
    Task,
    Status,
    Comment
)
from django.contrib.auth.models import User
from apps.task.forms import (
    CreateTask,
    TaskUpdateForm,
    CommentCreateForm

)
from django.shortcuts import (
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url='router:user:login')
def home_page(request):
    task = Task.objects.all().order_by('-created_at')
    context = {'tasks': task}
    return render(
        request=request,
        template_name='task/all_task.html',
        context=context
    )


@login_required(login_url='router:user:login')
def get_all_tasks(request):
    tasks = Task.objects.all().order_by('-created_at')
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
            return redirect("router:task:all-tasks")
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


# @login_required(login_url='router:user:login')
# def get_task_info_by_task_id(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     comments = Comment.objects.filter(
#         task=task_id
#     )
#     form = CommentCreateForm
#     context = {
#         "task": task,
#         "comments": comments,
#         "form": form
#     }
#     #####
#     return render(
#         request=request,
#         template_name='task/task_info.html',
#         context=context
#     )


@login_required(login_url='login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.delete()
    return redirect('router:task:all-tasks')


# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     form_class = CommentCreateForm
#
#     def is_ajax(self):
#         return self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'
#
#     def form_invalid(self, form):
#         if self.is_ajax():
#             return JsonResponse({'error': form.errors}, status=400)
#         return super().form_invalid(form)
#
#     def form_valid(self, form):
#         comment = form.save(commit=False)
#         comment.task_id = self.kwargs.get('pk')
#         comment.creator = self.request.user
#         comment.parent_id = form.cleaned_data.get('parent')
#         comment.save()
#
#         if self.is_ajax():
#             return JsonResponse({
#                 'is_child': comment.is_child_node(),
#                 'id': comment.id,
#                 'creator': comment.creator.username,
#                 'parent_id': comment.parent_id,
#                 'time_create': comment.time_create.strftime('%Y-%b-%d %H:%M:%S'),
#                 'avatar': comment.creator.profile.avatar.url,
#                 'content': comment.content,
#                 'get_absolute_url': comment.creator.profile.get_absolute_url()
#             }, status=200)
#
#         return redirect(comment.task.get_absolute_url())
#
#     def handle_no_permission(self):
#         return JsonResponse({'error': 'Необходимо авторизоваться для добавления комментариев'}, status=400)


class ReplyCommentView(View):
    def post(self, request, comment_id):
        parent_comment = Comment.objects.get(pk=comment_id)
        new_comment = Comment(
            text=request.POST['reply_text'],
            user=request.user,
            task=parent_comment.task,
            parent=parent_comment
        )
        new_comment.save()
        return redirect('router:task:task-info', task_id=parent_comment.task.id)


@login_required
def add_comment(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        Comment.objects.create(task=task, user=request.user, text=request.POST['comment_text'])
        return redirect('task-info', task_id=task.id)
    return render(request, 'tasks/add_comment.html', {'task': task})


@login_required
def task_info(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        if 'comment_text' in request.POST:
            Comment.objects.create(task=task, user=request.user, text=request.POST['comment_text'])
            return redirect('task-info', task_id=task.id)
    return render(request, 'task/task_info.html', {'task': task})

