"""
Tests for dankware.multithread module.
"""

import time

import pytest

from dankware import multithread


class TestMultithread:
    """Tests for the multithread function."""

    def test_basic_multithread(self):
        """Test basic multithread without arguments."""
        counter = {"value": 0}

        def increment():
            counter["value"] += 1

        multithread(increment, 5, progress_bar=False)
        assert counter["value"] == 5

    def test_multithread_with_list(self):
        """Test multithread with list input."""
        results = []

        def append_double(x):
            results.append(x * 2)

        multithread(append_double, 5, [1, 2, 3, 4, 5], progress_bar=False)
        assert sorted(results) == [2, 4, 6, 8, 10]

    def test_multithread_with_two_lists(self):
        """Test multithread with two list inputs."""
        results = []

        def add(a, b):
            results.append(a + b)

        list1 = [1, 2, 3]
        list2 = [10, 20, 30]
        multithread(add, 3, list1, list2, progress_bar=False)
        assert sorted(results) == [11, 22, 33]

    def test_multithread_with_constant(self):
        """Test multithread with list and constant value."""
        results = []

        def multiply(x, factor):
            results.append(x * factor)

        multithread(multiply, 5, [1, 2, 3, 4, 5], 10, progress_bar=False)
        assert sorted(results) == [10, 20, 30, 40, 50]

    def test_multithread_invalid_threads(self):
        """Test that invalid thread count raises ValueError."""

        def dummy():
            pass

        with pytest.raises(ValueError, match="positive integer"):
            multithread(dummy, 0, progress_bar=False)

    def test_multithread_worker_exception(self):
        """Test that unhandled exception in worker propagates."""

        def failing_worker():
            raise ZeroDivisionError("boom")

        with pytest.raises(ZeroDivisionError, match="boom"):
            multithread(failing_worker, 2, progress_bar=False)

    def test_multithread_timing(self):
        """Test that multithread is actually parallel."""

        def sleep_func():
            time.sleep(0.1)

        start = time.time()
        multithread(sleep_func, 10, progress_bar=False)
        elapsed = time.time() - start

        # Should complete in ~0.1s if parallel, not 1s
        assert elapsed < 0.5
