"""Tests for Graph 1."""

import pytest


@pytest.fixture
def init_g():
    """Fixture for initializing g()."""
    from graph_1 import G
    g = G()
    return g


def test_newly_initialized_graph_all_nodes(init_g):
    """Test that an empty graph has all_nodes."""
    assert init_g.all_nodes == []
    assert len(init_g.all_nodes) == 0


def test_newly_initialized_graph_all_edges(init_g):
    """Test that an empty graph has all_edges."""
    assert init_g.all_edges == []
    assert len(init_g.all_edges) == 0


def test_new_graph_nodes_function(init_g):
    """Test that an empty graph has no nodes."""
    assert init_g.nodes() == []


def test_new_graph_edges_function(init_g):
    """Test that an empty graph has no edges."""
    assert init_g.edges() == []


def test_add_nodes_to_empty_graph(init_g):
    """Test that the add_node fn works on an empty graph."""
    init_g.add_node(500)
    assert len(init_g.all_nodes) == 1
    assert init_g.nodes() == [500]


def test_add_multiple_nodes_to_graph(init_g):
    """Test adding multiple nodes to a graph."""
    init_g.add_node(5)
    init_g.add_node(15)
    init_g.add_node(115)
    init_g.add_node(1115)
    assert len(init_g.all_nodes) == 4
    assert init_g.nodes() == [5, 15, 115, 1115]


# def test_size_of_deque(init_g):
#     """Test that the size method is functional."""
#     d = Deque()
#     d.append(1)
#     assert d.size() == 1
#     d.append(2)
#     d.append(3)
#     assert d.size() == 3
