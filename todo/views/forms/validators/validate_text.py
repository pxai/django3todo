from django.core.exceptions import ValidationError

def validate_text(value):
    print("Validating value % ")
    if not "task" in value:
        raise ValidationError("Text must contain task word")
    else:
        return value