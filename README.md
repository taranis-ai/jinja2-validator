# jinja2-validator

## Overview
The `jinja2-validator` library provides a simple way to validate Jinja2 templates. It checks if the provided template strings are valid and can be used in applications that require template rendering.

## Installation
You can install the `jinja2-validator` library using pip. Run the following command:

```
pip install jinja2-validator
```

## Usage
To use the `jinja2-validator`, you need to import the `TemplateValidator` class from the library. Here is a simple example:

```python
from jinja2_validator import TemplateValidator

validator = TemplateValidator()

# Valid template
valid_template = "Hello {{ name }}!"
is_valid = validator.validate(valid_template)
print(is_valid)  # Output: True

# Invalid template
invalid_template = "Hello {{ name !"
is_valid = validator.validate(invalid_template)
print(is_valid)  # Output: False
```

## Features
- Validates Jinja2 templates.
- Returns `True` for valid templates and `False` for invalid ones.
- Custom exceptions for handling validation errors.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.