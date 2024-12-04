import random
import threading
import time

def alien_loop(depth=None, thread_id=0):
    def safeguard():
        nonlocal depth
        if not hasattr(safeguard, "counter"):
            safeguard.counter = {}
        if thread_id not in safeguard.counter:
            safeguard.counter[thread_id] = 0
        safeguard.counter[thread_id] += 1

        # Randomly reset the function and depth every 3rd call per thread
        if safeguard.counter[thread_id] % 3 == 0:
            global alien_loop
            alien_loop = original_loop
            depth = random.randint(2, 5)  # Randomize depth for this thread

        # Reset global function if tampered with
        global alien_loop
        if alien_loop is not original_loop:
            alien_loop = original_loop

    if depth is None:
        depth = random.randint(3, 7)  # Randomize initial depth for each thread

    original_loop = alien_loop  # Preserve the original definition

    if depth <= 0:
        print(f"Thread {thread_id}: Alien server complete.")
        return

    safeguard()  # Restore state dynamically

    # Simulate random alien code
    code = random.choice([
        "x = 5",
        "y = x + 2",
        f"print(f'Thread {thread_id}, Depth {depth}: still running...')",
        "z = y * 10"
    ])
    exec(code)

    # Recursive call or spawn a new thread
    if random.choice([True, False]):
        # Recursive call
        alien_loop(depth - 1, thread_id)
    else:
        # Spawn a new thread with a new ID
        new_thread_id = thread_id + 1
        thread = threading.Thread(target=alien_loop, args=(random.randint(3, 7), new_thread_id))
        thread.start()
        thread.join()  # Wait for the thread to complete
