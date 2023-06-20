# We can specify what items should be made available for import from this `directory_module_with_filtered_imports`
# module. The purpose of this __init__.py file is to indicate to the end user that they should use (and depend on)
# only the items imported in this __init__.py file. Every thing else in this directory is subject to change and should
# not be depended upon.

from .main import this_function_will_be_imported

# We can import `this_function_will_be_imported` without having to reference `main`:
# from rain.directory_module_with_filtered_imports import this_function_will_be_imported

# Since $REPO_ROOT/src/rain/__init__.py imports `this_function_will_be_imported`, we can also do this:
# from rain import this_function_will_be_imported
# (this is the recommended way)

# But, note that the end user can import the other items in this directory
# from rain.directory_module_with_filtered_imports.utils import helper_function_1
