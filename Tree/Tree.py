class TreeNode:
    def __init__(self, name, position):
        """
        Enter the value of node
        :param name: name of the employee
        :param position: position of the employee
        """
        self.name = name
        self.position = position
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

    def print_full_tree(self, level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|-" if self.parent else ""
        print(f"{prefix}{self.name} ({self.position})")
        if self.children:
            for child in self.children:
                child.print_full_tree(level)

    def print_name(self,level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|-" if self.parent else ""
        print(f"{prefix}{self.name}")
        if self.children:
            for child in self.children:
                child.print_name(level)

    def print_position(self,level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|-" if self.parent else ""
        print(f"{prefix}{self.position}")
        if self.children:
            for child in self.children:
                child.print_position(level)

def build_tree():
    root = TreeNode("Phuong","Department President")

    science_president = TreeNode("Peter","Science President")
    leader1 = TreeNode("John","Group 1 Leader")
    leader1.add_child(TreeNode("Jessica","Presenter"))
    leader1.add_child(TreeNode("Chris","Experimenter"))
    leader1.add_child(TreeNode("Jessica","Papers Researcher"))
    leader2 = TreeNode("Loan","Group 2 Leader")

    social_president = TreeNode("Christina","Social Recruitment")
    social_president.add_child(TreeNode("Henry","Recruiment Manager"))
    social_president.add_child(TreeNode("Luna","Policy Manager"))

    science_president.add_child(leader1)
    science_president.add_child(leader2)

    root.add_child(science_president)
    root.add_child(social_president)

    return root

if __name__ == '__main__':
    tree = build_tree()
    print("Full tree of name and position:")
    tree.print_full_tree(3)
    print("Full tree of name:")
    tree.print_name(3)
    print("Full tree of position:")
    tree.print_position(3)