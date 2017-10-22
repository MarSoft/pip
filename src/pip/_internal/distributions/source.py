"""
"""

from pip._internal.models.distribution import Distribution


class SourceDistribution(Distribution):
    """Represents a distribution installed from an archive


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

    def archive(self, location):
        # type: (Path) -> None
        """Save an archive of the given distribution in location
        """
        raise NotImplementedError()
