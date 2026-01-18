"""
Tests for dankware.files module.
"""

import os
import pytest
import tempfile
from dankware.files import (
    get_file_hash,
    ensure_dir,
    safe_filename,
    get_file_size,
    human_readable_size,
    read_text,
    write_text,
    file_exists,
    dir_exists,
)


class TestGetFileHash:
    """Tests for get_file_hash function."""

    def test_sha256_hash(self, tmp_path):
        """Test SHA256 hash calculation."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello World")

        hash_val = get_file_hash(str(test_file), "sha256")
        assert len(hash_val) == 64  # SHA256 produces 64 hex chars

    def test_md5_hash(self, tmp_path):
        """Test MD5 hash calculation."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello World")

        hash_val = get_file_hash(str(test_file), "md5")
        assert len(hash_val) == 32  # MD5 produces 32 hex chars


class TestEnsureDir:
    """Tests for ensure_dir function."""

    def test_create_single_dir(self, tmp_path):
        """Test creating a single directory."""
        new_dir = tmp_path / "new_folder"
        result = ensure_dir(str(new_dir))
        assert new_dir.exists()
        assert new_dir.is_dir()

    def test_create_nested_dirs(self, tmp_path):
        """Test creating nested directories."""
        nested = tmp_path / "a" / "b" / "c"
        result = ensure_dir(str(nested))
        assert nested.exists()


class TestSafeFilename:
    """Tests for safe_filename function."""

    def test_remove_invalid_chars(self):
        """Test that invalid characters are replaced."""
        assert safe_filename('file<>:"/\\|?*.txt') == "file_________.txt"

    def test_strip_dots_and_spaces(self):
        """Test stripping leading/trailing dots and spaces."""
        assert safe_filename("  ..file.txt..  ") == "file.txt"

    def test_empty_result(self):
        """Test that empty result becomes 'unnamed'."""
        assert safe_filename("...") == "unnamed"


class TestHumanReadableSize:
    """Tests for human_readable_size function."""

    def test_bytes(self):
        """Test bytes formatting."""
        assert "B" in human_readable_size(500)

    def test_kilobytes(self):
        """Test KB formatting."""
        assert "KB" in human_readable_size(1500)

    def test_megabytes(self):
        """Test MB formatting."""
        assert "MB" in human_readable_size(1500000)

    def test_gigabytes(self):
        """Test GB formatting."""
        assert "GB" in human_readable_size(1500000000)


class TestReadWriteText:
    """Tests for read_text and write_text functions."""

    def test_write_and_read(self, tmp_path):
        """Test writing and reading text file."""
        test_file = tmp_path / "test.txt"
        content = "Hello, World!\nLine 2"

        write_text(str(test_file), content)
        result = read_text(str(test_file))

        assert result == content


class TestExistsChecks:
    """Tests for file_exists and dir_exists functions."""

    def test_file_exists(self, tmp_path):
        """Test file_exists function."""
        test_file = tmp_path / "exists.txt"
        test_file.write_text("test")

        assert file_exists(str(test_file)) is True
        assert file_exists(str(tmp_path / "not_exists.txt")) is False

    def test_dir_exists(self, tmp_path):
        """Test dir_exists function."""
        assert dir_exists(str(tmp_path)) is True
        assert dir_exists(str(tmp_path / "not_exists")) is False
