import threading

from starlette.testclient import TestClient

from tests.conftest import APITestCase
from tests.const import PREFIX


def call_post_ticket(client: TestClient):
    post = client.post(f"{PREFIX}/tickets")


class TestTicket(APITestCase):

    def test_ticket(self, client: TestClient):
        thread1 = threading.Thread(target=call_post_ticket, args=[client])
        thread2 = threading.Thread(target=call_post_ticket, args=[client])
        # Start the threads
        thread1.start()
        thread2.start()

        # The main thread waits for both threads to finish
        thread1.join()
        thread2.join()
