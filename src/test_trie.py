"""Module containing functions that test Trie Tree."""
from trie import Trie
import pytest


@pytest.fixture
def trie():
    """Fixture that creates empty instance of Trie Tree."""

    return Trie()


def test_new_trie_table_has_size_of_zero(trie):
    """Function to test new empty Trie Tree is initialized with a size of 0."""

    assert trie.size() == 0
    assert trie._size == 0


def test_new_trie_table_root_node_has_empty_children_and_correct_letter(trie):
    """Function that tests a newly created Trie Tree has a root Node
    initialized with the '*' character and an empty children dictionary."""

    t = trie
    assert t.root.letter == '*'
    assert t.root.children == {}
    assert t.root.parent is None


def test_insert_on_new_trie_adds_node_to_root_node_children_dict(trie):
    """Function that tests a newly inserted node populates root nodes
    children dictionary, that it's an instance of a Node, and that the last
    letter inserted is a terminal node."""
    from trie import Node

    t = trie
    assert t.root.children == {}
    t.insert('a')
    assert len(t.root.children) == 1
    assert isinstance(t.root.children['a'], Node)
    assert t.root.children['a'].children['$'].letter == '$'


def test_insert_on_new_trie_adds_parent_to_new_node(trie):
    """Function that tests a newly inserted node's parent pointer points at
    the previous node in the tree."""

    t = trie
    t.insert('ab')
    assert t.root.children['a'].parent.letter == '*'
    assert t.root.children['a'].children['b'].parent.letter == 'a'
    assert t.root.children['a'].children['b'].children['$'].parent.letter == 'b'


def test_insert_with_same_word_doesnt_increase_size(trie):
    """Function that tests inserting the same word twice will not effect the
    Trie Trees size."""

    t = trie
    t.insert('apples')
    t.insert('apples')
    assert t.size() == 1


def test_insert_adds_nodes_containing_letter_values(trie):
    """Function that tests insert method of Trie Tree adds new nodes in the
    correct order, from the root node down, with the correct pointers to the
    consequent nodes which contain letters of the given string."""

    t = trie
    assert t.root.letter == '*'
    t.insert('apple')
    assert t.root.children['a'].letter == 'a'
    assert t.root.children['a'].children['p'].letter == 'p'
    assert t.root.children['a'].children['p'].children['p'].letter == 'p'
    assert t.root.children['a'].children['p'].children['p'].children['l'].letter == 'l'
    assert t.root.children['a'].children['p'].children['p'].children['l'].children['e'].letter == 'e'


def test_size_method_returns_correct_trie_size_one_insert(trie):
    """Function that tests that the size method on the Trie Tree returns the
    correct size of the table, where each letter represents one node in the
    table and the size indicates how many nodes exist in the table."""

    t = trie
    t.insert('apple')
    assert t.size() == 1


def test_size_method_returns_correct_trie_size_multiple_inserts(trie):
    """Function that tests that the size method on the Trie Tree returns the
    correct size of the table, where each letter represents one node in the
    table and the size indicates how many nodes exist in the table, given
    multiple inserts."""

    t = trie
    t.insert('apple')
    t.insert('application')
    t.insert('python')
    assert t.size() == 3


def test_contains_method_returns_true_if_string_in_table(trie):
    """Function that tests the contains method of the Trie Tree returns True
    if the string given exists within the table."""

    t = trie
    t.insert('apple')
    assert t.contains('apple')


def test_contains_method_returns_false_if_string_not_in_table(trie):
    """Function that tests the contains method of the Trie Tree returns False
    if the string given does not exist within the table."""

    t = trie
    t.insert('apple')
    assert t.contains('pinecone') is False
    assert t.contains('application') is False
    assert t.contains('app') is False


def test_remove_raise_exception_if_trie_empty(trie):
    """Function that tests remove method of Trie Tree raises a KeyError
    if the Trie Tree is empty."""

    t = trie
    with pytest.raises(KeyError):
        assert t.remove('yoyo')


def test_remove_raise_exception_if_given_word_partially_in_trie(trie):
    """Function that tests remove method of Trie Tree raises a KeyError
    if the given word is partially, but not completely, in Trie Tree."""

    t = trie
    t.insert('apple')
    with pytest.raises(KeyError):
        assert t.remove('app')
        assert t.remove('apples')


def test_remove_deletes_one_word_from_trie_and_reduces_size(trie):
    """Function that tests remove method of the Trie Tree deletes the given
    word from the Trie Tree and reduces the size of the table by one,
    if Trie Tree only contains one word."""

    t = trie
    t.insert('apple')
    assert t.size() == 1
    t.remove('apple')
    assert t.size() == 0
    assert t.root.children == {}


def test_remove_deletes_multiple_words_from_trie_and_reduces_size(trie):
    """Function that tests remove method of the Trie Tree deletes the given
    word from the Trie Tree and reduces the size of the table by one,
    if Trie Tree contains multiple words."""

    t = trie
    t.insert('apple')
    t.insert('giraffe')
    assert t.size() == 2
    t.remove('apple')
    t.remove('giraffe')
    assert t.size() == 0
    assert t.root.children == {}


def test_remove_deletes_only_correct_word_of_multiple_similar_words(trie):
    """Function that tests remove method of the Trie Tree deletes the given
    word, but does not effect any similar words that differ only slightly."""

    t = trie
    t.insert('apple')
    t.insert('app')
    t.insert('apples')
    assert t.size() == 3
    t.remove('app')
    assert t.contains('app') is False
    assert t.contains('apple')
    assert t.contains('apples')
    t.remove('apples')
    assert t.contains('apples') is False
    assert t.contains('apple')
    assert t.size() == 1


def test_private_remove_helper_method_deletes_all_given_words(trie):
    """Function that tests the _remove_helper method of the Trie Tree deletes
    all given words from Trie given correct parent and child nodes."""

    t = trie
    t.insert('abc')
    parent = t.root.children['a'].children['b'].children['c']
    child = t.root.children['a'].children['b'].children['c'].children['$']
    assert t.contains('abc')
    t._remove_helper(parent, child)
    assert t.contains('abc') is False
    assert t.root.children == {}
