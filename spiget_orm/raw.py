"""Some global functions for API requests."""
from functools import lru_cache

from requests import get
from requests.models import Response


@lru_cache
def _raw_api_answer(url: str) -> Response:
    """Private method for make raw API requests. It is **NOT A PART** of public API.

    Args:
        url: URL to request.

    Returns:
        Raw ``requests.models.Response`` object.
    """
    headers = {"User-Agent": "spiget-orm"}
    return get("https://api.spiget.org/v2/" + url, headers=headers)
