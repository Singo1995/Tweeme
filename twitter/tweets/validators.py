from django.core.exceptions import ValidationError

def validate_content(value):
    content = value
    if content == "cde":
        raise ValidationError("Content cannot be cde")
    return value