#!/usr/bin/env python

"""
Given a list of folders in a filesystem and the name of a folder to remove,
return the new list of folders after removal.

Examples:

$ removeFolder([“/a”,”/a/b”,”/c/d”,”/c/d/e”,”/c/f”, “/c/f/g”], ‘c’)
$ [“/a”,”/a/b”]

$ removeFolder([“/a”,”/a/b”,”/c/d”,”/c/d/e”,”/c/f”, “/c/f/g”], ‘d’) $ [“/a”,”/a/b”,”/c”,”/c/f”, “/c/f/g”]
"""


def remove_folder(existing, target):
    all_folders = set()
    for folder in existing:
        path = folder.split("/")
        for i in range(1, len(path)):   # strip off root directory
            component = path[i]
            if component == target:
                break
            all_folders.add("/".join(path[:i+1]))
    return sorted(list(all_folders))



def test_example1():
    assert remove_folder(["/a","/a/b","/c/d","/c/d/e","/c/f", "/c/f/g"], 'c') \
            == ["/a","/a/b"]


def test_example2():
    assert remove_folder(["/a","/a/b","/c/d","/c/d/e","/c/f", "/c/f/g"], 'd') \
            == ["/a","/a/b","/c","/c/f", "/c/f/g"]
