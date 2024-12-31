from dataclasses import dataclass, field


@dataclass
class XmasTree:
    """Class to represent a programmatically generated line Xmas Tree."""

    trunk_width: int
    trunk_height: int
    tree_width: int
    tree_height: int
    tree_levels: int
    tree_line_width: int
    points: list = field(default_factory=list)

    _trunk_width: int = field(init=False, repr=False, default=20)
    _trunk_height: int = field(init=False, repr=False, default=40)
    _tree_width: int = field(init=False, repr=False, default=100)
    _tree_height: int = field(init=False, repr=False, default=200)
    _tree_levels: int = field(init=False, repr=False, default=5)
    _tree_line_width: int = field(init=False, repr=False, default=20)
    _has_been_initialized: bool = field(init=False, repr=False, default=False)

    def __post_init__(self):
        self._has_been_initialized = True
        self._calculate_points()

    def _calculate_points(self):
        # Calculate the points of the tree
        points = []
        # Iterate over the levels of the tree
        for level in range(self.tree_levels):
            # Calculate the level height and width
            level_height = self.tree_height // self.tree_levels
            level_width = (
                self.tree_width * (self.tree_levels - level) // self.tree_levels
            )
            # Create the points on the left and right side of the tree
            points.append((-level_width // 2, -level * level_height))
            points.append((level_width // 2, -level * level_height))
        # Add the top point of the tree
        points.append((0, -self.tree_height))
        # Set the points of the tree
        self.points = points

    @property
    def trunk_width(self) -> int:
        return self._trunk_width

    @trunk_width.setter
    def trunk_width(self, value: int) -> None:
        if value < 1:
            raise ValueError("Trunk width must be greater than 0")
        self._trunk_width = value

    @property
    def trunk_height(self) -> int:
        return self._trunk_height

    @trunk_height.setter
    def trunk_height(self, value: int) -> None:
        if value < 1:
            raise ValueError("Trunk height must be greater than 0")
        self._trunk_height = value

    @property
    def tree_width(self) -> int:
        return self._tree_width

    @tree_width.setter
    def tree_width(self, value: int) -> None:
        if value < 1:
            raise ValueError("Tree width must be greater than 0")
        self._tree_width = value
        if self._has_been_initialized:
            self._calculate_points()

    @property
    def tree_height(self) -> int:
        return self._tree_height

    @tree_height.setter
    def tree_height(self, value: int) -> None:
        if value < 1:
            raise ValueError("Tree height must be greater than 0")
        self._tree_height = value
        if self._has_been_initialized:
            self._calculate_points()

    @property
    def tree_levels(self) -> int:
        return self._tree_levels

    @tree_levels.setter
    def tree_levels(self, value: int) -> None:
        if value < 1:
            raise ValueError("Tree levels must be greater than 0")
        self._tree_levels = value
        if self._has_been_initialized:
            self._calculate_points()

    @property
    def tree_line_width(self) -> int:
        return self._tree_line_width

    @tree_line_width.setter
    def tree_line_width(self, value: int) -> None:
        if value < 1:
            raise ValueError("Tree line width must be greater than 0")
        self._tree_line_width = value
