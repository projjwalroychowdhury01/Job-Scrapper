import subprocess, sys

def test_cli_runs_successfully():
    # Run the CLI with a dummy keyword; it should exit with code 0
    result = subprocess.run([
        sys.executable,
        "-m",
        "job_scrapper",
        "--keyword",
        "engineer",
    ], capture_output=True, text=True)
    assert result.returncode == 0
