"""
Tests for dankware.download module.
"""

from unittest.mock import MagicMock, patch

import pytest

from dankware import download_file, download_multiple
from dankware.exceptions import DownloadError


class TestDownload:
    """Tests for download utilities."""

    @patch("dankware.download.requests.get")
    def test_download_file_success(self, mock_get, tmp_path):
        """Test successful file download."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {"content-length": "12"}
        mock_response.iter_content.return_value = [b"hello ", b"world!"]
        mock_get.return_value = mock_response

        dest_file = tmp_path / "downloaded.txt"
        result = download_file("https://example.com/test.txt", str(dest_file), progress=False)

        assert result == str(dest_file)
        assert dest_file.read_bytes() == b"hello world!"

    @patch("dankware.download.requests.get")
    def test_download_file_into_directory(self, mock_get, tmp_path):
        """Test file download when destination is a directory."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {"content-length": "5"}
        mock_response.iter_content.return_value = [b"dank!"]
        mock_get.return_value = mock_response

        dest_dir = tmp_path / "subdir"
        dest_dir.mkdir()
        result = download_file("https://example.com/file.bin", str(dest_dir), progress=False)

        expected_file = dest_dir / "file.bin"
        assert result == str(expected_file)
        assert expected_file.read_bytes() == b"dank!"

    @patch("dankware.download.requests.get")
    def test_download_file_failure(self, mock_get, tmp_path):
        """Test that download failure raises DownloadError."""
        import requests

        mock_get.side_effect = requests.RequestException("Network down")

        with pytest.raises(DownloadError, match="Failed to download"):
            download_file("https://example.com/missing.bin", str(tmp_path / "fail.bin"), progress=False)

    @patch("dankware.download.download_file")
    def test_download_multiple(self, mock_download, tmp_path):
        """Test downloading multiple files with callback."""
        mock_download.side_effect = lambda url, dest, progress: f"{dest}/file"
        completed = []

        def on_complete(url, path):
            completed.append((url, path))

        urls = ["https://a.com/1", "https://b.com/2"]
        results = download_multiple(urls, str(tmp_path), progress=False, on_complete=on_complete)

        assert len(results) == 2
        assert len(completed) == 2
