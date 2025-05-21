from jinja2 import Environment, TemplateSyntaxError
from exceptions import TemplateValidationError # Changed from .exceptions

class TemplateValidator:
    @staticmethod
    def validate(template_str: str, raise_exception: bool = False) -> bool:
        try:
            # Create a Jinja2 environment and compile the template
            env = Environment()
            env.from_string(template_str)
            return True
        except TemplateSyntaxError as e:
            if raise_exception:
                raise TemplateValidationError(f"Template syntax error: {str(e)}")
            return False
        except Exception as e:
            if raise_exception:
                raise TemplateValidationError(f"Template validation failed: {str(e)}")
            return False