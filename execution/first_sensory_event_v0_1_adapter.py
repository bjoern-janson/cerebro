#!/usr/bin/env python3
"""Gap-bounded execution adapter for FIRST_SENSORY_EVENT_V0.1.

This adapter performs exactly one source operation: resolve the frozen R01/A1
coordinate through GitHub's commit endpoint using the SHA-only media type.
It does not request or parse commit metadata, diffs, trees, paths, or content.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OWNER = "bjoern-janson"
REPOSITORY = "interface-induced-computational-geometry"
EXPECTED_ANCHOR = "7cea701ab34ed536a5cc0050c3188c6c900fafe3"
ENDPOINT = (
    f"https://api.github.com/repos/{OWNER}/{REPOSITORY}/commits/{EXPECTED_ANCHOR}"
)
ACCEPT = "application/vnd.github.sha"
USER_AGENT = "cerebro-first-sensory-event-v0.1"
MAX_SHA_RESPONSE_BYTES = 128
DEFAULT_TIMEOUT_SECONDS = 10.0


class Outcome(str, Enum):
    RESOLVED = "RESOLVED"
    NOT_RESOLVED = "NOT_RESOLVED"
    ACCESS_BLOCKED = "ACCESS_BLOCKED"
    SOURCE_CONFLICT = "SOURCE_CONFLICT"
    IDENTITY_MISMATCH = "IDENTITY_MISMATCH"
    TRANSPORT_FAILURE = "TRANSPORT_FAILURE"
    UNEXPECTED_RESPONSE = "UNEXPECTED_RESPONSE"


@dataclass(frozen=True)
class ResolutionResult:
    outcome: Outcome
    http_status: int | None = None


def _request() -> Request:
    return Request(
        ENDPOINT,
        headers={
            "Accept": ACCEPT,
            "User-Agent": USER_AGENT,
        },
        method="GET",
    )


def resolve_exact_anchor(timeout: float = DEFAULT_TIMEOUT_SECONDS) -> ResolutionResult:
    """Execute only the frozen exact-anchor resolution operation."""

    request = _request()

    try:
        with urlopen(request, timeout=timeout) as response:
            status = response.getcode()
            if status != 200:
                return ResolutionResult(Outcome.UNEXPECTED_RESPONSE, status)

            raw = response.read(MAX_SHA_RESPONSE_BYTES + 1)
            if len(raw) > MAX_SHA_RESPONSE_BYTES:
                return ResolutionResult(Outcome.UNEXPECTED_RESPONSE, status)

            try:
                resolved = raw.decode("ascii").strip()
            except UnicodeDecodeError:
                return ResolutionResult(Outcome.UNEXPECTED_RESPONSE, status)

            if resolved == EXPECTED_ANCHOR:
                return ResolutionResult(Outcome.RESOLVED, status)
            return ResolutionResult(Outcome.IDENTITY_MISMATCH, status)

    except HTTPError as exc:
        if exc.code == 404:
            return ResolutionResult(Outcome.NOT_RESOLVED, exc.code)
        if exc.code in (401, 403):
            return ResolutionResult(Outcome.ACCESS_BLOCKED, exc.code)
        if exc.code == 409:
            return ResolutionResult(Outcome.SOURCE_CONFLICT, exc.code)
        return ResolutionResult(Outcome.UNEXPECTED_RESPONSE, exc.code)
    except (URLError, TimeoutError, OSError):
        return ResolutionResult(Outcome.TRANSPORT_FAILURE, None)


def main() -> int:
    result = resolve_exact_anchor()
    print(result.outcome.value)

    return {
        Outcome.RESOLVED: 0,
        Outcome.NOT_RESOLVED: 2,
        Outcome.ACCESS_BLOCKED: 3,
        Outcome.SOURCE_CONFLICT: 4,
        Outcome.IDENTITY_MISMATCH: 5,
        Outcome.TRANSPORT_FAILURE: 6,
        Outcome.UNEXPECTED_RESPONSE: 7,
    }[result.outcome]


if __name__ == "__main__":
    sys.exit(main())
