"""Base Class for all Distributions
"""

import abc

from pip._vendor.six import add_metaclass


# NOTE: Figure out what all attributes/methods would be needed on this.

@add_metaclass(abc.ABCMeta)
class Distribution(object):
    """Abstraction for dealing with various distribution formats
    """

    def __init__(self, location):
        # type: (Link) -> None
        super(Distribution, self).__init__()

        self.location = location

    @abc.abstractproperty
    def name(self):
        # type: () -> str
        raise NotImplementedError()

    @abc.abstractproperty
    def version(self):
        # type: () -> Version
        raise NotImplementedError()

    @abc.abstractmethod
    def prepare(self):
        """Prepare for performing operations
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def load_metadata(self):
        # type: () -> None
        """Load basic information such as the name of the package, version etc.

        This information comes dist-info or egg-info.
        """
        raise NotImplementedError()

    @abc.abstractproperty
    def can_be_installed(self):
        # type: () -> bool
        """Whether this distribution can even be installed on this system
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def install(self, location):
        # type: (Path) -> None
        """Install self into location.
        """
        raise NotImplementedError()
