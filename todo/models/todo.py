class Todo(models.Model):
    """A model for todo"""
    task = models.CharField(max_length=400)
    active = models.BooleanField(default=True)
    status = models.CharField(choices=(
            (0, "To do"),
            (1, "Doing"),
            (2, "Done"),
        ),
        max_length=1
    )
    task_type = models.ForeignKey("TaskType")
