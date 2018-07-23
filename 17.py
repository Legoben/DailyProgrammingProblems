# # attempt
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
# second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file
# file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For
# example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length
# is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the length of the longest absolute path to a
# file in the abstracted file system. If there is no file in the system, return 0.


import re

def is_file(f):
    return f.find(".") != -1


def find_longest(path, level=0):
    print(level, path)

    next_newline = path.find("\n")
    if next_newline == -1:
        print("Return", len(path) if is_file(path) else 0)
        return len(path.replace("\t", "")) if is_file(path) else 0

    cur_file = path[:next_newline]
    print("cur", cur_file)

    if is_file(cur_file):
        print("Return", len(cur_file))
        return len(cur_file.replace("\t", ""))

    longest = 0

    print(re.split("\n[\t]{"+str(level)+"}(?!\t)", path[next_newline:]) if level != 0 else [path])

    for p in re.split("\n[\t]{"+str(level)+"}(?!\t)", path[next_newline:]) if level != 0 else [path]:
        longest = max(len(cur_file) + find_longest(p, level + 1), longest)

    print("Return", longest)
    return longest


if __name__ == "__main__":
    print(find_longest("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print("=======")
    print(find_longest("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))