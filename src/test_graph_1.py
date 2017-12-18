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


def test_add_one_edge(init_g):
    """Test adding an edge."""
    init_g.add_node(5)
    init_g.add_node(10)
    init_g.add_edge(5, 10)
    assert (5, 10) in init_g.edges()


def test_add_multiple_edges(init_g):
    """Test adding an edge."""
    init_g.add_node(5)
    init_g.add_node(10)
    init_g.add_node(15)
    init_g.add_edge(5, 10)
    init_g.add_edge(15, 10)
    init_g.add_edge(5, 15)
    assert (5, 10) in init_g.edges()
    assert (15, 10) in init_g.edges()
    assert (5, 15) in init_g.edges()


def test_add_edge_when_val_doesnt_exist(init_g):
    """Test adding an edge."""
    init_g.add_node(20)
    init_g.add_edge(20, 400)
    assert (20, 400) in init_g.edges()


def test_add_edge_when_no_vals_exist(init_g):
    """Test adding an edge."""
    init_g.add_edge(1, 2)
    assert (1, 2) in init_g.edges()


def test_del_node(init_g):
    """Test deleting existant node."""
    init_g.add_node(5)
    init_g.del_node(5)
    assert len(init_g.all_nodes) == 0


def test_del_node_index_error(init_g):
    """Test deleting a node that doesnt exist."""
    init_g.add_node(5)
    with pytest.raises(IndexError):
        assert init_g.del_node(25)


def test_del_node_and_its_edges(init_g):
    """Test that del node deletes val edges too."""
    init_g.add_node(5)
    init_g.add_node(30)
    init_g.add_edge(30, 10)
    init_g.del_node(30)
    assert len(init_g.all_edges) == 0


def test_del_edge(init_g):
    """Test that del_edge deletes edge."""
    init_g.add_edge(25, 30)
    init_g.add_edge(1, 2)
    init_g.del_edge(1, 2)
    assert init_g.edges() == [(25, 30)]


def test_del_edge_that_doesnt_exist(init_g):
    """Test that del_edge deletes edge that is nonexistent."""
    init_g.add_edge(25, 30)
    init_g.add_edge(1, 2)
    with pytest.raises(IndexError):
        assert init_g.del_edge(50, 50)


def test_has_node_false(init_g):
    """Assert has node for False."""
    assert init_g.has_node(200) is False


def test_has_node_true(init_g):
    """Assert has node for False."""
    init_g.add_node(75)
    print(init_g.nodes())
    assert init_g.has_node(75) is True


def test_neighbors_true(init_g):
    """Test that neighbors returns neighbors when they do exist."""
    init_g.add_edge(1, 2)
    init_g.add_edge(1, 4)
    init_g.add_edge(1, 15)
    print(init_g.all_nodes)
    assert init_g.neighbors(1) == [2, 4, 15]


def test_neighbors_false(init_g):
    """Test that neighbors returns when they dont exist."""
    with pytest.raises(IndexError):
        init_g.neighbors(1)


def test_adjacent_true(init_g):
    """Test that adjacent returns true when nodes connected."""
    init_g.add_edge(1, 2)
    print(init_g.nodes())
    print(init_g.edges())
    assert init_g.adjacent(1, 2) is True


def test_adjacent_false(init_g):
    """Test that adjacent returns false when nodes unconnected."""
    init_g.add_node(1)
    init_g.add_node(2)
    assert init_g.adjacent(1, 2) is False


def test_adjacent_error_handling(init_g):
    """Test IndexError for adjacent."""
    init_g.add_node(13)
    with pytest.raises(IndexError):
        init_g.adjacent(13, 35)
