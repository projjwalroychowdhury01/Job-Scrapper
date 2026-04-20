import urllib.parse


def _encode_keyword(keyword: str) -> str:
    """URL‑encode a search keyword for query parameters.

    Uses ``quote_plus`` to ensure spaces become ``+`` as expected by many
    search engines.
    """
    return urllib.parse.quote_plus(keyword)


def build_indeed_url(keyword: str) -> str:
    """Construct an Indeed job‑search URL for the given *keyword*.

    Example::

        >>> build_indeed_url("software engineer")
        'https://www.indeed.com/jobs?q=software+engineer'
    """
    encoded = _encode_keyword(keyword)
    return f"https://www.indeed.com/jobs?q={encoded}"

# Placeholder for future site helpers
# def build_linkedin_url(keyword: str) -> str:
#     ...
