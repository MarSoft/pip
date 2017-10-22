"""
"""

from pip._internal.models.distribution import Distribution


class DirectoryDistribution(Distribution):
    """Represents a distribution unpacked in a directory.

    This is used for pip install /path/to/dir
    """

    @property
    def name(self):
        # type: () -> str
        raise NotImplementedError()

    @property
    def version(self):
        # type: () -> Version
        raise NotImplementedError()

    @property
    def can_be_installed(self):
        # type: () -> bool
        raise NotImplementedError()

    def prepare(self):
        raise NotImplementedError()

    def load_metadata(self):
        # type: () -> None
        raise NotImplementedError()

    def install(self, location):
        # type: (Path) -> None
        raise NotImplementedError()
