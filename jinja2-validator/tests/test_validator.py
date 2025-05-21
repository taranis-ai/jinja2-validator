import pytest
# from jinja2 import Template, TemplateSyntaxError
from validator import TemplateValidator
from exceptions import TemplateValidationError

def test_valid_template():
    valid_template = "{{ variable }}"
    validator = TemplateValidator()
    assert validator.validate(valid_template) is True

def test_invalid_template():
    invalid_template = "{{ variable "
    validator = TemplateValidator()
    assert validator.validate(invalid_template) is False

def test_empty_template():
    empty_template = ""
    validator = TemplateValidator()
    assert validator.validate(empty_template) is True

def test_template_with_comments():
    comment_template = "{# This is a comment #} {{ variable }}"
    validator = TemplateValidator()
    assert validator.validate(comment_template) is True

def test_template_with_control_structure():
    control_structure_template = "{% if condition %} {{ variable }} {% endif %}"
    validator = TemplateValidator()
    assert validator.validate(control_structure_template) is True

def test_template_with_syntax_error():
    syntax_error_template = "{% if condition % {{ variable }} {% endif %}"
    validator = TemplateValidator()
    with pytest.raises(TemplateValidationError):
        validator.validate(syntax_error_template, raise_exception=True)