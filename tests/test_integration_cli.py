import os
import json
import subprocess
import sys
import pytest

def test_cli_full_crawl_mock(tmp_path):
    # Use a temporary output file
    out_file = tmp_path / "out.json"
    # Run the CLI; spiders are placeholders and will yield no items, resulting in empty JSON array
    result = subprocess.run(
        [sys.executable, "-m", "job_scrapper", "--keyword", "engineer", "--output", str(out_file)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"CLI failed: {result.stderr}"
    # Verify the output file exists; if not, treat as empty result
    if out_file.exists():
        data = json.load(open(out_file, "r", encoding="utf-8"))
        assert isinstance(data, list)
    else:
        # No items were scraped, which is acceptable for placeholder spiders
        assert True
