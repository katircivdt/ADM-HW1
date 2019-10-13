# 1-)XML 1 - FIND THE SCORE

# this function iterate over all child node prints the total number of attrib

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    return sum([len(child.attrib) for child in root.iter()])


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# 2-)XML2 - Find the Maximum Depth
#??????