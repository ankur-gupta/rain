import sys
import logging

# Get the file-level logger for this file. This logger won't have an effect on the package's logger.
file_level_logger = logging.getLogger(__name__)

# Get the "main" package-level logger from $REPO_ROOT/rain/__init__.py. This is the parent of all other loggers
# defined in the package.
pkg_level_logger = logging.getLogger('rain')


def print_logger_details(logger: logging.Logger, name: str):
    print(f'{name}: logger.root={logger.root}')
    print(f'{name}: logger.handlers={logger.handlers}')


def log_message(msg: str):
    file_level_logger.info(f'file_level_logger: rain.logging_example.main.log_message(): {msg}')
    pkg_level_logger.info(f'pkg_level_logger: rain.logging_example.main.log_message(): {msg}')


def logger_demo():
    print_logger_details(file_level_logger, 'file_level_logger')
    # file_level_logger: logger.root=<RootLogger root (WARNING)>
    # file_level_logger: logger.handlers=[]

    print_logger_details(pkg_level_logger, 'pkg_level_logger')
    # pkg_level_logger: logger.root=<RootLogger root (WARNING)>
    # pkg_level_logger: logger.handlers=[<NullHandler (NOTSET)>]

    # Since, this logger is still set to NullHandler(), nothing gets printed to stdout.
    log_message('1')  # nothing gets printed to stdout

    # Add a stdout handler to file_level_logger
    file_level_logger.setLevel(logging.DEBUG)
    file_level_logger.addHandler(logging.StreamHandler(sys.stdout))

    print_logger_details(file_level_logger, 'file_level_logger')
    # file_level_logger: logger.root=<RootLogger root (WARNING)>
    # file_level_logger: logger.handlers=[<StreamHandler <stdout> (NOTSET)>]

    print_logger_details(pkg_level_logger, 'pkg_level_logger')
    # pkg_level_logger: logger.root=<RootLogger root (WARNING)>
    # pkg_level_logger: logger.handlers=[<NullHandler (NOTSET)>]

    # Only the `file_level_logger` is set to print to stdout. The `pkg_level_logger` will not print anything.
    log_message('2')
    # file_level_logger: rain.logging_example.main.log_message(): 2

    # Add a stdout handler to pkg_level_logger
    pkg_level_logger.setLevel(logging.DEBUG)
    pkg_level_logger.addHandler(logging.StreamHandler(sys.stdout))

    print_logger_details(file_level_logger, 'file_level_logger')
    # file_level_logger: logger.root=<RootLogger root (WARNING)>
    # file_level_logger: logger.handlers=[<StreamHandler <stdout> (NOTSET)>]

    print_logger_details(pkg_level_logger, 'pkg_level_logger')
    # pkg_level_logger: logger.root=<RootLogger root (WARNING)>
    # pkg_level_logger: logger.handlers=[<NullHandler (NOTSET)>, <StreamHandler <stdout> (NOTSET)>]

    # Now, both loggers will print to stdout.
    log_message('3')
    # file_level_logger: rain.logging_example.main.log_message(): 3
    # file_level_logger: rain.logging_example.main.log_message(): 3
    # pkg_level_logger: rain.logging_example.main.log_message(): 3

    # Note that both `file_level_logger` and `pkg_level_logger` have `root` logger as their parent.
    print(file_level_logger.root)  # <RootLogger root (WARNING)>
    print(pkg_level_logger.root)  # <RootLogger root (WARNING)>
    print(file_level_logger.root is pkg_level_logger.root)  # True
    print(file_level_logger.root.handlers)  # []
