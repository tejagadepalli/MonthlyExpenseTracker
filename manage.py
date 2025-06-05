#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the default settings module for the 'expense_project'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_project.settings')

    try:
        # Try to import Django's execute_from_command_line utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Provide a more descriptive error if Django is not installed or accessible
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command line utility
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Check if the virtual environment is active
    if not hasattr(sys, 'real_prefix') and not (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    ):
        print("Warning: You are not in a virtual environment. It's recommended to use a virtual environment for Django projects.")
    
    main()
