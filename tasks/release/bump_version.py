"""Helper Commands for making releases
"""

import os

from .utils import ROOT, build_version, find_version, replace_in_file, Version

from invoke import task


def _bump_version_str(version_str, major=False, minor=False, patch=False,
                      dev=False, final=False):
    """Actual version bumping logic
    """
    old = build_version(version_str)

    # We assume every version bump would mean we enter development for the new
    # version which is basically the development flow anyway.
    if major:
        new = Version(old.major + 1, 0, 0, 0)
    elif minor:
        new = Version(old.major, old.minor + 1, 0, 0)
    elif patch:
        new = Version(old.major, old.minor, old.patch + 1, 0)
    elif dev:
        new_dev = old.dev + 1 if old.dev is not None else 0
        new = Version(old.major, old.minor, old.patch, new_dev)
    elif final:
        new = Version(old.major, old.minor, old.patch, None)
    else:
        msg = "Specify one of --major, --minor, --patch, --dev or --final"
        raise RuntimeError(msg)

    return ".".join(map(str, new[:3])) + (
        ".dev" + str(new.dev) if new.dev is not None else ""
    )

# Poor Man's Testing
assert _bump_version_str("2.0.0.dev0", dev=True) == "2.0.0.dev1"
assert _bump_version_str("2.0.1.dev1", minor=True) == "2.1.0.dev0"
assert _bump_version_str("2.1.0.dev1", patch=True) == "2.1.1.dev0"
assert _bump_version_str("2.1.2.dev1", major=True) == "3.0.0.dev0"
assert _bump_version_str("3.0.0.dev1", final=True) == "3.0.0"
assert _bump_version_str("3.0.0", dev=True) == "3.0.0.dev0"


@task(help={
    'major': "Bumps the major segment.",
    'minor': "Bumps the minor segment, retaining the major segment.",
    'patch': "Bumps the patch segment, retaining the major and minor segment.",
    'dev': "Bumps the dev segment, retaining the other segments.",
    'final': "Drops any dev segment in the version.",
})
def bump_version(ctx, major=False, minor=False, patch=False,
                 dev=False, final=False):
    """Bump the version in setup.py and pip/__init__.py

    Useful for keeping version information in sync and managing each release
    bump.
    """

    # These are the files containing the version string that we want to update.
    locations = [("setup.py",), ("src", "pip", "__init__.py")]

    # We read the version from the first location -- setup.py
    old = find_version(*locations[0])
    print("[release.bump-version] Current version is: {}".format(old))

    new = _bump_version_str(old, major, minor, patch, dev, final)
    print("[release.bump-version] Updated version will be: {}".format(new))

    for parts in locations:
        fname = os.path.abspath(os.path.join(ROOT, *parts))
        print("[release.bump-version] Writing to: {}".format(fname))
        replace_in_file(fname, old, new)
