"""Some global functions for API requests."""
from functools import lru_cache
from typing import Optional, Tuple, Union

from requests import get
from requests.models import Response


@lru_cache
def _raw_api_answer(url: str, **kwargs) -> Response:
    """Private method for make raw API requests. It is **NOT A PART** of public API.

    Args:
        url: URL to request.

    Returns:
        Raw ``requests.models.Response`` object.
    """
    headers = {"User-Agent": "spiget-orm"}
    return get("https://api.spiget.org/v2/" + url, headers=headers, **kwargs)


def _params_parser(*args: Tuple[str, Optional[Union[str, int]]]) -> str:
    """Private method for parse parameters. It is **NOT A PART** of public API.

    Args:
        *args: Parameters to parse. Format: ``(key, value), (key2, value)``.

    Returns:
        Parsed string.
    """
    ret = ""
    for key, value in args:
        if value is None:
            continue
        ret += "&".join(f"{key}={value}")
    return ret
