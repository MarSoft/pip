"""Helper Commands for making releases
"""

from .bump_version import bump_version
from .utils import find_version, version_locations

from invoke import task


@task
def check(ctx):
    # Check that the version in the various locations are in sync
    versions = {
        find_version(*parts) for parts in version_locations
    }

    if len(versions) != 1:
        raise Exception(
            "Got version mismatch: {}".format(",".join(sorted(versions)))
        )
    else:
        print("[release.check] version strings are in sync.")
