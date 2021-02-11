from collections import namedtuple

Version = namedtuple("Version", ["major", "minor", "patch"])

__version_info__ = Version(0, 1, 0)
__version__ = ".".join(map(str, __version_info__))
