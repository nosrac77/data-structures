"""Module that contains functions to test Hash Table."""
import pytest


@pytest.fixture
def my_hash():
    """Fixture which creates an instance of a HashTable, initialized with a
    table length of 500 and my simple hash."""
    from hash_table import HashTable

    return HashTable(500, 'my hash')


@pytest.fixture
def one_hash():
    """Fixture which creates an instance of a HashTable, initialized with a
    table length of 500 and my implementation of the One Step at a Time hash,
    a simplified version of the Jenkins hash."""
    from hash_table import HashTable

    return HashTable(500, 'one')


def test_new_hash_table_initialized_with_given_length_and_hash_type():
    """Function that tests a newly created instance of a HashTable has a table
    with a length matching the given value and a hash_type matching the given
    value."""
    from hash_table import HashTable

    h = HashTable(1234, 'Flerg')
    assert len(h.table) == 1234
    assert h.hash_type == 'Flerg'


def test_diff_hash_type_on_init_changes_hash_used(my_hash, one_hash):
    """Function that tests different inputs for hash_value when creating new
    instance of HashTable will changed the hash used, as per the spec."""

    m = my_hash
    o = one_hash
    assert m._hash('a') != o._hash('a')


def test_diff_hash_types_factor_in_capitalization(my_hash, one_hash):
    """Function that tests both hashing functions both factor in capitalization
    of the given character."""

    m = my_hash
    o = one_hash
    assert m._hash('a') != m._hash('A')
    assert o._hash('a') != o._hash('A')


def test_all_methods_raise_valueerror_if_not_str(my_hash):
    """Function that tests the get method of the Hash Table returns an empty
    list if the table holds no value at the given key."""

    m = my_hash
    with pytest.raises(ValueError):
        m._hash(1000)
        m.set(1000, 'nope')
        m.get(1000)


def test_set_method_adds_val_to_table_at(my_hash, one_hash):
    """Function that tests the set method of the Hash Table adds a value to
    the hash table at the given key. Function tests both implementations of the
    hash functions."""

    m = my_hash
    o = one_hash
    m_hash = m._hash('hello')
    o_hash = o._hash('hello')
    m.set('hello', 'world')
    o.set('hello', 'world')
    assert 'world' in m.table[m_hash]
    assert 'world' in o.table[o_hash]


def test_get_method_returns_empty_list_if_val_not_at_given(my_hash):
    """Function that tests the get method of the Hash Table returns an empty
    list if the table holds no value at the given key."""

    m = my_hash
    assert m.get('hello') == []


def test_get_method_returns_value_from_table_at(my_hash, one_hash):
    """Function that tests the get method of Hash Table returns the value
    held in the table at the given key."""

    m = my_hash
    m.set('Name', 'Carson')
    assert m.get('Name') == ['Carson']


def test_hash_table_works_given_huge_list_of_words():
    """Function that tests both types of hash functions successfully add values
    with the given key against an enormous list of words. The size of both Hash
    Tables will be the exact word count of the given file."""
    from hash_table import HashTable

    m = HashTable(99155, 'my hash')
    o = HashTable(99155, 'one')

    f = open("lots_of_words.txt", "r")
    words = f.readlines()
    for word in words:
        m.set(word, word)
        o.set(word, word)
        assert word in m.get(word)
        assert word in o.get(word)
    f.close()
