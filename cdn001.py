import requests
import time

# Test script
def test_cdn():
    # First request
    start = time.time()
    response1 = requests.get('http://localhost:8000/test1.txt')
    time1 = time.time() - start
    print(f"First request: {response1.text}")
    print(f"Time taken: {time1:.4f} seconds")

    # Second request (should be cached)
    start = time.time()
    response2 = requests.get('http://localhost:8000/test1.txt')
    time2 = time.time() - start
    print(f"\nSecond request: {response2.text}")
    print(f"Time taken: {time2:.4f} seconds")

    # You should see the second request is faster!

test_cdn()