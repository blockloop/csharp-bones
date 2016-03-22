#!/bin/env python

import sys


from py.path import local  # import local path object/class


def rename_files(root, pattern):
    """
    Iterate over all paths starting at root using ``~py.path.local.visit()``
    check if it is a file using ``~py.path.local.check(file=True)`` and
    rename it with a new basename with ``pattern`` stripped out.
    """

    for path in root.visit(rec=True):
        if path.check(file=True):
            path.rename(path.new(basename=path.basename.replace(pattern, "")))


def rename_dirs(root, pattern):
    """
    Iterate over all paths starting at root using ``~py.path.local.visit()``
    check if it is a directory using ``~py.path.local.check(dir=True)`` and
    rename it with a new basename with ``pattern`` stripped out.
    """

    for path in root.visit(rec=True):
        if path.check(dir=True):
            path.rename(path.new(basename=path.basename.replace(pattern, "")))


def main():
    """Define our main top-level entry point"""

    root = local(sys.argv[1])  # 1 to skip the program name
    pattern = sys.argv[2]

    if local(sys.argv[0]).purebasename == "renamefiles":
        rename_files(root, pattern)
    else:
        rename_dirs(root, pattern)


if __name__ == "__main__":
    """
    Python sets ``__name__`` (a global variable) to ``__main__`` when being called
    as a script/application. e.g: Python renamefiles or ./renamefiles
    """

    main()  # Call our main function
