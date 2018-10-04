"""DataLad demo extension"""

__docformat__ = 'restructuredtext'

from .version import __version__

# defines a datalad command suite
# this symbold must be indentified as a setuptools entrypoint
# to be found by datalad
command_suite = (
    # description of the command suite, displayed in cmdline help
    "DataLad revolutionary command suite",
    [
        # specification of a command, any number of commands can be defined
        (
            # importable module that contains the command implementation
            'datalad_revolution.revcmd',
            # name of the command class implementation in above module
            'RevCmd',
            # optional name of the command in the cmdline API
            'rev-cmd',
            # optional name of the command in the Python API
            'rev_cmd'
        ),
        # specification of a command, any number of commands can be defined
        (
            # importable module that contains the command implementation
            'datalad_revolution.revcreate',
            # name of the command class implementation in above module
            'RevCreate',
            # optional name of the command in the cmdline API
            'rev-create',
            # optional name of the command in the Python API
            'rev_create'
        ),
    ]
)

from datalad import setup_package
from datalad import teardown_package
