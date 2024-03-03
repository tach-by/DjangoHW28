from django.db import models
from django.contrib.auth.admin import User
from mptt.models import MPTTModel, TreeForeignKey


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Task(models.Model):
    title = models.CharField(max_length=30, default='Enter title: ')
    description = models.TextField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(
        Status,
        on_delete=models.SET(1),
        blank=True,
        null=True
    )

    date_started = models.DateField(help_text="Дата начала")
    deadline = models.DateField(help_text="Дата окончания")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def str(self):
        return f"{self.title[:10]}..."

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


# class Comment(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
#     username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
#     text = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.text

# class Comment(MPTTModel):
#     """
#     Модель древовидных комментариев
#     """
#
#     STATUS_OPTIONS = (
#         ('published', 'Опубликовано'),
#         ('draft', 'Черновик')
#     )
#
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача', related_name='comments')
#     creator = models.ForeignKey(User, verbose_name='Автор комментария', on_delete=models.CASCADE,
#                                 related_name='comments_author')
#     content = models.TextField(verbose_name='Текст комментария', max_length=3000)
#     time_create = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
#     time_update = models.DateTimeField(verbose_name='Время обновления', auto_now=True)
#     status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Статус поста', max_length=10)
#     parent = TreeForeignKey('self', verbose_name='Родительский комментарий', null=True, blank=True,
#                             related_name='children', on_delete=models.CASCADE)
#
#     class MTTMeta:
#         order_insertion_by = ('-time_create',)
#
#     class Meta:
#         db_table = 'app_comments'
#         indexes = [models.Index(fields=['-time_create', 'time_update', 'status', 'parent'])]
#         ordering = ['-time_create']
#         verbose_name = 'Комментарий'
#         verbose_name_plural = 'Комментарии'
#
#     def __str__(self):
#         return f'{self.creator}:{self.content}'


class Comment(models.Model):
    # Существующие поля
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    # Добавленное поле для ответа на комментарий
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')