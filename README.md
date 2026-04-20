# Job‑Scrapper

A Python CLI utility to scrape job listings from multiple sites, filter by experience level, and output a pretty‑printed JSON file.

## Installation

```bash
pip install -e .
```

## Usage

```bash
python -m job_scrapper --keyword <search-term> [options]
```

### Options
- `--keyword <term>` **(required)** – Search keyword (e.g., `python`, `engineer`).
- `--experience <range>` – Experience filter; one of `all`, `0-2`, `3-5`, `5+`. Default is `all`.
- `--output <path>` – Path to output JSON file (default `jobs.json`).
- `--verbose` – Enable Scrapy INFO logging.
```

## Example

```bash
python -m job_scrapper --keyword engineer --experience "3-5" --output engineer_jobs.json --verbose
```

This will crawl supported sites, filter jobs requiring 3‑5 years of experience, and write the results to `engineer_jobs.json`.

## Development

Run the test suite:
```bash
pytest -q
```

Pre‑commit hooks are configured for Black, Isort, and Flake8. Install and run them with:
```bash
pre-commit install
pre-commit run --all-files
```
