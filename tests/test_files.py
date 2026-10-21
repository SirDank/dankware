"""
Tests for dankware.files module.
"""

from dankware import (
    ensure_dir,
    get_file_hash,
    human_readable_size,
    list_files,
    safe_filename,
)


class TestGetFileHash:
    """Tests for get_file_hash function."""

    def test_sha256_hash(self, tmp_path):
        """Test SHA256 hash calculation."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello World", encoding="utf-8")

        hash_val = get_file_hash(str(test_file), "sha256")
        assert len(hash_val) == 64

    def test_md5_hash(self, tmp_path):
        """Test MD5 hash calculation."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello World", encoding="utf-8")

        hash_val = get_file_hash(str(test_file), "md5")
        assert len(hash_val) == 32


class TestEnsureDir:
    """Tests for ensure_dir function."""

    def test_create_single_dir(self, tmp_path):
        """Test creating a single directory."""
        new_dir = tmp_path / "new_folder"
        result = ensure_dir(str(new_dir))
        assert new_dir.exists()
        assert new_dir.is_dir()
        assert result == new_dir

    def test_create_nested_dirs(self, tmp_path):
        """Test creating nested directories."""
        nested = tmp_path / "a" / "b" / "c"
        result = ensure_dir(str(nested))
        assert nested.exists()
        assert result == nested


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


class TestListFiles:
    """Tests for list_files function."""

    def test_list_files_shallow_and_recursive(self, tmp_path):
        """Test listing files with glob patterns."""
        (tmp_path / "file1.txt").write_text("1", encoding="utf-8")
        (tmp_path / "file2.py").write_text("2", encoding="utf-8")
        sub = tmp_path / "sub"
        sub.mkdir()
        (sub / "file3.py").write_text("3", encoding="utf-8")

        shallow_py = list(list_files(str(tmp_path), "*.py", recursive=False))
        assert len(shallow_py) == 1

        recursive_py = list(list_files(str(tmp_path), "*.py", recursive=True))
        assert len(recursive_py) == 2
