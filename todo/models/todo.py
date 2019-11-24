from django.db import models
from django.utils.translation import gettext_lazy as _

class Todo(models.Model):
    """A model for todo"""
    task = models.CharField(_("task"), max_length=400, help_text=_("Enter task info"))
    active = models.BooleanField(default=True)
    status = models.CharField(choices=(
            (0, "To do"),
            (1, "Doing"),
            (2, "Done"),
        ),
        max_length=1
    )
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    task_type = models.ForeignKey("TaskType",on_delete=models.CASCADE, default=1)

    # Other options: help_text, verbose_name, default, null(True), blank(True), primary_key (true)

    # Metadata
