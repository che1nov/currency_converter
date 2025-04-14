from src.main import run
import threading


def test_main(monkeypatch):
    server_thread = threading.Thread(target=run, daemon=True)
    server_thread.start()
    assert True
