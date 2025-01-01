import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest
from xtreegen.xmas_tree import XmasTree


@pytest.mark.parametrize("trunk_width", [0, 20, 30])
@pytest.mark.parametrize("trunk_height", [0, 40, 50])
@pytest.mark.parametrize("tree_width", [0, 100, 200])
@pytest.mark.parametrize("tree_height", [0, 200, 300])
@pytest.mark.parametrize("tree_levels", [0, 5, 6])
@pytest.mark.parametrize("tree_line_width", [0, 1, 10])
def test_init(
    trunk_width, trunk_height, tree_width, tree_height, tree_levels, tree_line_width
):
    # Test the initialization of the XmasTree class with invalid values
    if any(
        [
            trunk_width < 1,
            trunk_height < 1,
            tree_width < 1,
            tree_height < 1,
            tree_levels < 1,
            tree_line_width < 1,
        ]
    ):
        with pytest.raises(ValueError):
            XmasTree(
                trunk_width,
                trunk_height,
                tree_width,
                tree_height,
                tree_levels,
                tree_line_width,
            )
    # Test the initialization of the XmasTree class with valid values
    else:
        xmas_tree = XmasTree(
            trunk_width,
            trunk_height,
            tree_width,
            tree_height,
            tree_levels,
            tree_line_width,
        )
        assert xmas_tree.trunk_width == trunk_width
        assert xmas_tree.trunk_height == trunk_height
        assert xmas_tree.tree_width == tree_width
        assert xmas_tree.tree_height == tree_height
        assert xmas_tree.tree_levels == tree_levels
        assert xmas_tree.tree_line_width == tree_line_width
        assert xmas_tree.points is not None
        assert len(xmas_tree.points) == 2 * tree_levels + 1


def test_default_values():
    # Test the default values of the XmasTree class
    xmas_tree = XmasTree()
    assert xmas_tree.trunk_width == XmasTree._trunk_width
    assert xmas_tree.trunk_height == XmasTree._trunk_height
    assert xmas_tree.tree_width == XmasTree._tree_width
    assert xmas_tree.tree_height == XmasTree._tree_height
    assert xmas_tree.tree_levels == XmasTree._tree_levels
    assert xmas_tree.tree_line_width == XmasTree._tree_line_width
    assert xmas_tree.points is not None
    assert len(xmas_tree.points) == 2 * xmas_tree.tree_levels + 1


@pytest.mark.parametrize("trunk_width", [0, 20, 30])
@pytest.mark.parametrize("trunk_height", [0, 40, 50])
@pytest.mark.parametrize("tree_width", [0, 100, 200])
@pytest.mark.parametrize("tree_height", [0, 200, 300])
@pytest.mark.parametrize("tree_levels", [0, 5, 6])
@pytest.mark.parametrize("tree_line_width", [0, 1, 10])
def test_setters(
    trunk_width, trunk_height, tree_width, tree_height, tree_levels, tree_line_width
):
    # Test the setters of the XmasTree class with invalid values
    xmas_tree = XmasTree()
    if trunk_width < 1:
        with pytest.raises(ValueError):
            xmas_tree.trunk_width = trunk_width
    if trunk_height < 1:
        with pytest.raises(ValueError):
            xmas_tree.trunk_height = trunk_height
    if tree_width < 1:
        with pytest.raises(ValueError):
            xmas_tree.tree_width = tree_width
    if tree_height < 1:
        with pytest.raises(ValueError):
            xmas_tree.tree_height = tree_height
    if tree_levels < 1:
        with pytest.raises(ValueError):
            xmas_tree.tree_levels = tree_levels
    if tree_line_width < 1:
        with pytest.raises(ValueError):
            xmas_tree.tree_line_width = tree_line_width
    # Test the setters of the XmasTree class with valid values
    if all(
        [
            trunk_width > 0,
            trunk_height > 0,
            tree_width > 0,
            tree_height > 0,
            tree_levels > 0,
            tree_line_width > 0,
        ]
    ):
        xmas_tree.trunk_width = trunk_width
        assert xmas_tree.trunk_width == trunk_width
        xmas_tree.trunk_height = trunk_height
        assert xmas_tree.trunk_height == trunk_height
        xmas_tree.tree_width = tree_width
        assert xmas_tree.tree_width == tree_width
        xmas_tree.tree_height = tree_height
        assert xmas_tree.tree_height == tree_height
        xmas_tree.tree_levels = tree_levels
        assert xmas_tree.tree_levels == tree_levels
        xmas_tree.tree_line_width = tree_line_width
        assert xmas_tree.tree_line_width == tree_line_width
        assert xmas_tree.points is not None
        assert len(xmas_tree.points) == 2 * tree_levels + 1
