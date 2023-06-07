class Tree:
    def __init__(self, data, value=0):
        self.data = data
        self.value = value
        self.children = []

    def __repr__(self):
        return self.data

    def __eq__(self, other):
        if isinstance(other, Tree):
            return self.data == other.data
        return False

    def add_parent(self, parent_node):
        assert isinstance(parent_node, Tree)
        parent_node.add_child(self)

    def add_child(self, child_node):
        assert isinstance(child_node, Tree)
        self.children.append(child_node)

    def calculate_value(self):
        if len(self.children) > 0:
            self.value = sum(child.calculate_value()
                             for child in self.children)
        return self.value


    def print_tree(self, level=0, is_last_child=False):
        indent = ""
        branch = "└──"
        if level > 0:
            indent = " " * (4 * level - 2)
            if not is_last_child:
                branch = "├──"

        print(f"{indent}{branch} {self.data} {self.value}")
        for i, child in enumerate(self.children):
            child.print_tree(level + 1, i == len(self.children) - 1)

    def print_firstchild(self):
        for i in self.children:
            print(i, i.value)

    def print_valuechild(self):
        lys = []
        for i in self.children:
            lys.append(i.value)
        return lys

    def add_value(self, data, value):
        if self.data == data:
            self.value += value
        else:
            for child in self.children:
                child.add_value(data, value)


# t = Tree('*')
# samsung = Tree('samsung')
# enzo = Tree('enzo', 20)
# bastian = Tree('bastian', 14)
# samsung.add_child(enzo)
# samsung.add_child(bastian)
# t.add_child(samsung)

# apple = Tree('apple')
# harald = Tree('harald', value=3)
# cleo = Tree('cleo')
# apple.add_child(harald)
# apple.add_child(cleo)
# t.add_child(apple)


# t.add_value("cleo", 10)
# t.add_value("cleo", 5)

# t.calculate_value()

# t.print_tree()
# t.print_firstchild()
