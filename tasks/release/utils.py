
import collections
import tempfile
import os
import re
import shutil


version_locations = [("setup.py",), ("src", "pip", "__init__.py")]

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_VERSION_PRAGMA_MESSAGE = "note: version managed using invoke"
_VERSION_RE = (
    r'^.*\s*=\s*"([^"]*)",?\s*\#\s*' + _VERSION_PRAGMA_MESSAGE + "$"
)

Version = collections.namedtuple(
    "Version", ["major", "minor", "patch", "dev"]
)


def read(*parts):
    with open(os.path.join(ROOT, *parts)) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(_VERSION_RE, version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def build_version(version_str):
    parts = version_str.split(".")
    try:
        # Convert into integers and parse the dev version if it's there.
        # pip doesn't use pre or post release info so, this script doesn't
        # account for it.
        return Version(
            major=int(parts[0]), minor=int(parts[1]), patch=int(parts[2]),
            dev=None if len(parts) < 4 else int(parts[3][3:])
        )
    except (IndexError, ValueError) as e:
        raise RuntimeError("Could not parse version: {}".format(version_str))


def replace_in_file(fpath, old, new):
    #Create temp file
    fh, abs_path = tempfile.mkstemp()

    with os.fdopen(fh,'w') as new_file, open(fpath) as old_file:
        for line in old_file:
            if _VERSION_PRAGMA_MESSAGE in line:
                new_file.write(line.replace(old, new))
            else:
                new_file.write(line)

    # Conservative Saving
    shutil.move(fpath, fpath + ".tmp")
    shutil.move(abs_path, fpath)
    os.remove(fpath + ".tmp")
