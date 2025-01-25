import requests
import time
import threading

SERVER_URL = "http://localhost:7887"

def post_wish(num_requests=10):
    """Sendet num_requests POST-Requests an /wishes."""
    for i in range(num_requests):
        data = {"wish": f"Wish {i}", "status": 1}
        try:
            response = requests.post(f"{SERVER_URL}/wishes", json=data)
            #Optional: 
            print(response.status_code, response.text)
        except Exception as e:
            print(f"Error in POST request: {e}")

def get_wishes(num_requests=10):
    """Sendet num_requests GET-Requests an /wishes."""
    for i in range(num_requests):
        try:
            response = requests.get(f"{SERVER_URL}/wishes")
            # Optional: print(response.status_code, len(response.json()))
        except Exception as e:
            print(f"Error in GET request: {e}")

def put_wish(num_requests=10):
    """Sendet num_requests PUT-Requests an /wishes/1."""
    for i in range(num_requests):
        data = {"wish": f"Updated Wish {i}", "status": 2}
        try:
            response = requests.put(f"{SERVER_URL}/wishes/1", json=data)
            # Optional: print(response.status_code, response.text)
        except Exception as e:
            print(f"Error in PUT request: {e}")


if __name__ == "__main__":
    # Anzahl Threads und Requests pro Thread:
    num_threads = 10
    requests_per_thread = 20

    print("Starting load test...")

    start_time = time.time()

    threads = []

    # Erzeuge parallel GET-, POST und PUT -Threads
    for _ in range(num_threads):
        t_post = threading.Thread(target=post_wish, args=(requests_per_thread,))
        t_get = threading.Thread(target=get_wishes, args=(requests_per_thread,))
        t_put = threading.Thread(target=put_wish, args=(requests_per_thread,))
        threads.append(t_post)
        threads.append(t_get)
        threads.append(t_put)

    # Starte alle Threads
    for t in threads:
        t.start()

    # Warte, bis alle fertig sind
    for t in threads:
        t.join()

    end_time = time.time()
    duration = end_time - start_time

    total_requests = num_threads * requests_per_thread * 2  # weil wir pro Thread 1x POST, 1x GET
    rps = total_requests / duration

    print(f"Total Requests: {total_requests}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Requests per second (approx): {rps:.2f}")
