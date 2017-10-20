import invoke

from . import generate
from . import vendoring
from . import release

ns = invoke.Collection(generate, vendoring, release)
