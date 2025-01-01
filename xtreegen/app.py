import tkinter as tk
from .xmas_tree import XmasTree

MAX_TRUNK_RATIO = 0.25


class XmasTreeApp:
    """A class to draw a Christmas tree using a GUI."""

    def __init__(self, main: tk.Tk, canvas_width: int = 600, canvas_height: int = 400):
        """Initialize the XmasTreeApp class.

        Parameters:
        -----------
        main : tk.Tk
            The main window of the application.
        canvas_width : int
            The width of the canvas.
        canvas_height : int
            The height of the canvas.
        """
        # Set the max trunk height
        self.MAX_TRUNK_HEIGHT = int(MAX_TRUNK_RATIO * canvas_height)
        # Set the max tree height
        self.MAX_TREE_HEIGHT = canvas_height - self.MAX_TRUNK_HEIGHT

        # Store the main window
        self.main = main

        # Store the canvas dimensions
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        # Calculate the center of the canvas
        self.center_x = canvas_width // 2
        self.center_y = canvas_height - self.MAX_TRUNK_HEIGHT

        # Add a title to the main window
        self.main.title("Xmas Tree App")

        # Create a canvas to draw the Christmas tree
        self.canvas = tk.Canvas(
            self.main, bg="white", width=canvas_width, height=canvas_height
        )
        self.canvas.pack()

        # Initialize the Christmas tree
        self.xmas_tree = XmasTree()

        # Add sliders for the tree parameters
        self.add_sliders()

        # Draw the Christmas tree
        self.draw_tree()

    def add_sliders(self):
        """Add sliders to control the tree parameters."""
        # Create a container frame for the sliders in a 2x3 grid
        frame_top = tk.Frame(self.main)
        frame_top.pack()
        frame_bottom = tk.Frame(self.main)
        frame_bottom.pack()

        # Trunk width slider
        self.trunk_width_slider = tk.Scale(
            self.main,
            from_=1,
            to=100,
            variable=tk.IntVar(value=self.xmas_tree.trunk_width),
            orient="horizontal",
            label="Trunk Width",
            command=self.update_trunk_width,
        )
        self.trunk_width_slider.pack(in_=frame_top, side="left")

        # Trunk height slider
        self.trunk_height_slider = tk.Scale(
            self.main,
            from_=1,
            to=self.MAX_TRUNK_HEIGHT,
            variable=tk.IntVar(value=self.xmas_tree.trunk_height),
            orient="horizontal",
            label="Trunk Height",
            command=self.update_trunk_height,
        )
        self.trunk_height_slider.pack(in_=frame_top, side="left")

        # Tree width slider
        self.tree_width_slider = tk.Scale(
            self.main,
            from_=1,
            to=300,
            variable=tk.IntVar(value=self.xmas_tree.tree_width),
            orient="horizontal",
            label="Tree Width",
            command=self.update_tree_width,
        )
        self.tree_width_slider.pack(in_=frame_top, side="left")

        # Tree height slider
        self.tree_height_slider = tk.Scale(
            self.main,
            from_=1,
            to=self.MAX_TREE_HEIGHT,
            variable=tk.IntVar(value=self.xmas_tree.tree_height),
            orient="horizontal",
            label="Tree Height",
            command=self.update_tree_height,
        )
        self.tree_height_slider.pack(in_=frame_bottom, side="left")

        # Tree levels slider
        self.tree_levels_slider = tk.Scale(
            self.main,
            from_=1,
            to=10,
            variable=tk.IntVar(value=self.xmas_tree.tree_levels),
            orient="horizontal",
            label="Tree Levels",
            command=self.update_tree_levels,
        )
        self.tree_levels_slider.pack(in_=frame_bottom, side="left")

        # Tree line width slider
        self.tree_line_width_slider = tk.Scale(
            self.main,
            from_=1,
            to=20,
            variable=tk.IntVar(value=self.xmas_tree.tree_line_width),
            orient="horizontal",
            label="Tree Line Width",
            command=self.update_tree_line_width,
        )
        self.tree_line_width_slider.pack(in_=frame_bottom, side="left")

    def update_trunk_width(self, event):
        """Update the trunk width of the Christmas tree."""
        self.xmas_tree.trunk_width = self.trunk_width_slider.get()
        self.draw_tree()

    def update_trunk_height(self, event):
        """Update the trunk height of the Christmas tree."""
        self.xmas_tree.trunk_height = self.trunk_height_slider.get()
        self.draw_tree()

    def update_tree_width(self, event):
        """Update the tree width of the Christmas tree."""
        self.xmas_tree.tree_width = self.tree_width_slider.get()
        self.draw_tree()

    def update_tree_height(self, event):
        """Update the tree height of the Christmas tree."""
        self.xmas_tree.tree_height = self.tree_height_slider.get()
        self.draw_tree()

    def update_tree_levels(self, event):
        """Update the tree levels of the Christmas tree."""
        self.xmas_tree.tree_levels = self.tree_levels_slider.get()
        self.draw_tree()

    def update_tree_line_width(self, event):
        """Update the tree line width of the Christmas tree."""
        self.xmas_tree.tree_line_width = self.tree_line_width_slider.get()
        self.draw_tree()

    def draw_tree(self):
        """Draw the Christmas tree on the canvas."""
        # Clear the canvas
        self.canvas.delete("all")

        # Draw the trunk
        trunk_width = self.xmas_tree.trunk_width
        trunk_height = self.xmas_tree.trunk_height
        self.canvas.create_rectangle(
            self.center_x - trunk_width // 2,
            self.center_y,
            self.center_x + trunk_width // 2,
            self.center_y + trunk_height,
            fill="brown",
        )

        # Draw the tree
        points = self.xmas_tree.points
        for i in range(len(points) - 1):
            self.canvas.create_line(
                self.center_x + points[i][0],
                self.center_y + points[i][1],
                self.center_x + points[i + 1][0],
                self.center_y + points[i + 1][1],
                width=self.xmas_tree.tree_line_width,
                fill="green",
            )
