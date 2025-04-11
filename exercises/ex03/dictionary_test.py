"""Dictionary Functions"""

__author__ = "730568756"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_basic():
    """Test invert with a basic dictionary."""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_use_case():
    """Test invert with another use case."""
    assert invert({"c": "5", "z": "7", "y": "8"}) == {"5": "c", "7": "z", "8": "y"}


def test_invert_edge_case():
    """Test invert with a empty dictionary."""
    assert invert({}) == {}


def test_favorite_color_basic():
    """Test favorite_color with a clear most popular color."""
    assert (
        favorite_color({"Bob": "blue", "Brooke": "blue", "Paige": "orange"}) == "blue"
    )


def test_favorite_color_ties():
    """Test favorite_color with a tie."""
    assert (
        favorite_color(
            {"Bob": "blue", "Brooke": "blue", "Paige": "orange", "Meadow": "orange"}
        )
        == "blue"
    )


def test_favorite_color_edge_case():
    """Test favorite_color with an empty dictionary."""
    assert favorite_color({}) == ""


def test_count_basic():
    """Test count with a list of repeated elements."""
    assert count(["book", "page", "book"]) == {"book": 2, "page": 1}


def test_count_unique():
    """Test count with a list of no repeated items."""
    assert count(["book", "page", "cover", "title"]) == {
        "book": 1,
        "page": 1,
        "cover": 1,
        "title": 1,
    }


def test_count_edge_case():
    """Test count with empty list."""
    assert count([]) == {}


def test_bin_len_basic():
    """Test bin_len with words of one length."""
    assert bin_len(["age", "fox"]) == {3: {"age", "fox"}}


def test_bin_len_multiple():
    """Test bin_len with words of different lengths."""
    assert bin_len(["age", "year"]) == {3: {"age"}, 4: {"year"}}


def test_bin_len_edge_case():
    """Test bin_len with an empty list."""
    assert bin_len([]) == {}
