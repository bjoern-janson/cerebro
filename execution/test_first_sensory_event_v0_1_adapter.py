import io
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

import first_sensory_event_v0_1_adapter as adapter


class FakeResponse:
    def __init__(self, status, payload):
        self.status = status
        self._payload = payload
        self.read_size = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def getcode(self):
        return self.status

    def read(self, size=-1):
        self.read_size = size
        return self._payload[:size] if size >= 0 else self._payload


class AdapterTests(unittest.TestCase):
    def test_request_is_exact_sha_only_endpoint(self):
        request = adapter._request()
        self.assertEqual(request.full_url, adapter.ENDPOINT)
        self.assertEqual(request.get_method(), "GET")
        self.assertEqual(request.headers["Accept"], "application/vnd.github.sha")

    @patch.object(adapter, "urlopen")
    def test_exact_sha_resolves(self, mocked):
        response = FakeResponse(200, adapter.EXPECTED_ANCHOR.encode("ascii"))
        mocked.return_value = response
        result = adapter.resolve_exact_anchor()
        self.assertEqual(result.outcome, adapter.Outcome.RESOLVED)
        self.assertEqual(result.http_status, 200)
        self.assertEqual(response.read_size, adapter.MAX_SHA_RESPONSE_BYTES + 1)

    @patch.object(adapter, "urlopen")
    def test_wrong_sha_is_identity_mismatch(self, mocked):
        mocked.return_value = FakeResponse(200, b"0" * 40)
        result = adapter.resolve_exact_anchor()
        self.assertEqual(result.outcome, adapter.Outcome.IDENTITY_MISMATCH)

    @patch.object(adapter, "urlopen")
    def test_404_is_not_resolved(self, mocked):
        mocked.side_effect = HTTPError(adapter.ENDPOINT, 404, "Not Found", {}, io.BytesIO())
        result = adapter.resolve_exact_anchor()
        self.assertEqual(result.outcome, adapter.Outcome.NOT_RESOLVED)
        self.assertEqual(result.http_status, 404)

    @patch.object(adapter, "urlopen")
    def test_403_is_access_blocked(self, mocked):
        mocked.side_effect = HTTPError(adapter.ENDPOINT, 403, "Forbidden", {}, io.BytesIO())
        result = adapter.resolve_exact_anchor()
        self.assertEqual(result.outcome, adapter.Outcome.ACCESS_BLOCKED)

    @patch.object(adapter, "urlopen")
    def test_transport_failure_stays_transport_failure(self, mocked):
        mocked.side_effect = URLError("dns")
        result = adapter.resolve_exact_anchor()
        self.assertEqual(result.outcome, adapter.Outcome.TRANSPORT_FAILURE)
        self.assertIsNone(result.http_status)

    @patch.object(adapter, "urlopen")
    def test_oversized_response_is_rejected(self, mocked):
        mocked.return_value = FakeResponse(200, b"x" * (adapter.MAX_SHA_RESPONSE_BYTES + 2))
        result = adapter.resolve_exact_anchor()
        self.assertEqual(result.outcome, adapter.Outcome.UNEXPECTED_RESPONSE)


if __name__ == "__main__":
    unittest.main()
