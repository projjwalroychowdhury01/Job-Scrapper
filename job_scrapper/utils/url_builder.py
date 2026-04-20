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

def build_naukri_url(keyword: str) -> str:
    """Construct a Naukri job‑search URL for *keyword*.

    Example::
        >>> build_naukri_url('engineer')
        'https://www.naukri.com/jobs?q=engineer'
    """
    encoded = _encode_keyword(keyword)
    return f"https://www.naukri.com/jobs?q={encoded}"

def build_wellfound_url(keyword: str) -> str:
    """Construct a Wellfound job‑search URL for *keyword*.

    Example::
        >>> build_wellfound_url('engineer')
        'https://wellfound.com/jobs?q=engineer'
    """
    encoded = _encode_keyword(keyword)
    return f"https://wellfound.com/jobs?q={encoded}"

