class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|-" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_tree():
    root = TreeNode("Phuong")

    cellphones = TreeNode("Peter")
    smartphone = TreeNode("John")
    smartphone.add_child(TreeNode("Jessica"))
    cellphones.add_child(TreeNode("Google Pixel"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("ThinkPad"))
    laptop.add_child(TreeNode("Asus"))

    cellphones.add_child(smartphone)
    root.add_child(cellphones)
    root.add_child(tv)
    root.add_child(laptop)

    return root


if __name__ == "__main__":
    tree = build_tree()
    tree.print_tree(2)
