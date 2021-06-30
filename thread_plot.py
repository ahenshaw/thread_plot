from collections import defaultdict
from matplotlib.patches import Rectangle

class TreeNode:
    def __init__(self):
        self.count = 0
        self.children = defaultdict(TreeNode)

    def add(self, s):
        self.count += 1
        if s:
            k, rest = s[0], s[1:]
            self.children[k].add(rest)

    def __str__(self):
        retval = [f'{self.count}']
        for char in sorted(self.children):
            retval.append(f'{char}  {self.children[t]}')
        return '\n'.join(retval)

    def walk(self, index=0):
        for char in sorted(self.children):
            yield index, char, self.children[char].count
            for result in self.children[char].walk(index + 1):
                yield result
    
    def get_patches(self, index=0, base=0):
        offset = 0
        for char, child in sorted(self.children.items()):
                yield (index, base + offset, 1, child.count, char)
                for patch in child.get_patches(index+1, base + offset):
                    yield patch
                offset += child.count

def thread_plot(ax, colormap, data):
    root = TreeNode()
    max_len = 0
    for s in data:
        root.add(s)
        max_len = max(max_len, len(s))

    for (x, y, w, h, k) in root.get_patches():
        ax.add_patch(Rectangle((x, y), w, h, color=colormap[k]))
    ax.set_xlim(0, max_len)
    ax.set_ylim(0, len(data))

    
