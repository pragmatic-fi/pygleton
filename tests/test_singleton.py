"""
Tests for singleton decorator.
"""

from pygleton import singleton


def test_singleton() -> None:
    """Test singleton decorator."""

    @singleton()
    class Foo:  # pylint: disable=too-few-public-methods
        """Test class."""

        def __init__(self, number: int) -> None:

            self.number = number

    foo1 = Foo(1)
    foo2 = Foo(2)

    # it should be singleton
    assert foo1 is foo2

    # __init__ should be called only the first time
    assert foo1.number == 1
    assert foo2.number == 1

    # name and docstring should be preserved
    assert Foo.__name__ == "Foo"
    assert foo1.__doc__ == "Test class."


def test_singleton_recall_init() -> None:
    """Test singleton decorator if __init__ must be called every time."""

    @singleton(recall_init=True)
    class Foo:  # pylint: disable=too-few-public-methods
        """Test class."""

        def __init__(self, number: int) -> None:

            self.number = number

    foo1 = Foo(1)
    assert foo1.number == 1
    foo2 = Foo(2)
    assert foo2.number == 2

    # it should be singleton
    assert foo1 is foo2

    # name and docstring should be preserved
    assert Foo.__name__ == "Foo"
    assert foo1.__doc__ == "Test class."
