import sys
import os

# Add the parent directory (which is 'jinja2-validator/') to sys.path
# This allows tests to import modules like 'validator' and 'exceptions' directly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
