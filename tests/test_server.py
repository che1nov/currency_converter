import os
from unittest.mock import patch
from server import get_port


def test_port_import():
    assert isinstance(get_port(), int)
    assert get_port() == int(os.getenv("SERVER_PORT", 8000))


@patch.dict(os.environ, {"SERVER_PORT": "9000"})
def test_mocked_port():
    assert get_port() == 9000
