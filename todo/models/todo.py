from django.db import models

class Todo(models.Model):
    """A model for todo"""
    task = models.CharField(max_length=400, help_text="Enter task info")
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
    task_type = models.ForeignKey("TaskType",on_delete=models.CASCADE)

    # Other options: help_text, verbose_name, default, null(True), blank(True), primary_key (true)

    # Metadata
