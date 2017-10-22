"""
"""

from pip._internal.models.distribution import Distribution


class WheelDistribution(Distribution):
    """Represents a `.whl` file

    NOTE: pip._internal.wheel would largely get consolidated into this class.
          It might even make sense to break up this module and have a helper
          somewhere.
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
        # All the information is statically available
        # There is no preparation needed for processing
        pass

    def load_metadata(self):
        # type: () -> None
        raise NotImplementedError()

    def install(self, location):
        # type: (Path) -> None
        raise NotImplementedError()
