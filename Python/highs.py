# This is just some additional classes that I need to add because HiGHS didn't include stubs!

class highs_var:
    def __init__(self, name: str, index: int):
        self.name: str = name
        self.index: int = index