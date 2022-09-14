from __future__ import print_function
from collections import defaultdict
from collections.abc import Set


class TrieNode(Set):

    def __init__(self, iterable=()):
        self._children = defaultdict(TrieNode)
        self._end = False
        for element in iterable:
            self.add(element)

    def add(self, element):
        node = self
        for s in element:
            node = node._children[s]
        node._end = True

    def __contains__(self, element):
        node = self
        for k in element:
            if k not in node._children:
                return False
            node = node._children[k]
        return node._end

    def search(self, term):

        results = set()
        element = []

        def _search(m, node, i):

            element.append(m)
            if i == len(term):
                if node._end:
                    results.add(''.join(element))
            elif term[i] == '?':
                for k, child in node._children.items():
                    _search(k, child, i + 1)
            elif term[i] == '*':
                _search('', node, i + 1)
                for k, child in node._children.items():
                    _search(k, child, i)
            elif term[i] in node._children:
                _search(term[i], node._children[term[i]], i + 1)
            element.pop()
        _search('', self, 0)
        return results

    def __iter__(self):
        return iter(self.search('*'))

    def __len__(self):
        return sum(1 for _ in self)
