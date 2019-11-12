class TaskType(models.Model):
    """A model of task type"""
    name = models.CharField("Task type", max_length=200)