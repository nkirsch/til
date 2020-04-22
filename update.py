#!/usr/bin/env python

import os


HEADER="""
# Today I Learned

Wow! I only discovered this when [simonw/til](https://github.com/simonw/til)
appeared [on Hacker News](https://news.ycombinator.com/item?id=22920437), but
forked [aicioara/til](https://github.com/aicioara/til/) instead.
---

"""


def main():
    content = ""
    content += HEADER

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)

        content += "### {}\n\n".format(category)

        for file in files:
            name = os.path.basename(file).split('.')[0]
            name = " ".join(word.capitalize() for word in name.split('-'))
            content += "- [{}]({})\n".format(name, os.path.join(category, file))
        content += "\n"

    with open("README.md", "w") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
