#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Collatz-n with Max Tracker
# © Hiroshi Harada 2026 — Released under CC BY 4.0

def n_adic_integrated_lab():
    print("================================================")
    print("   n-adic Collatz Laboratory: Grand Edition   ")
    print("================================================")

    # --- 1. Universe Initialization ---
    try:
        n_input = input("Enter base n (e.g., 4): ")
        if not n_input:
            return
        n = int(n_input)
        if n < 2:
            print("Base must be 2 or greater.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    divisors = [d for d in range(n, 1, -1) if n % d == 0]

    # --- 2. Setting Modular Jump Constants ---
    c_vector = {}
    print(f"\nSetting modular constants c_r (n={n})")
    for r in range(1, n):
        is_reducible = any(r % d == 0 for d in divisors if d < n)
        if not is_reducible:
            while True:
                try:
                    c_val = int(input(f"  c_{r} (remainder {r}): "))
                    if (r + c_val) % n == 0:
                        c_vector[r] = c_val
                        break
                    else:
                        print(f"  Error: {r} + {c_val} is not divisible by {n}.")
                except ValueError:
                    print("Please enter a number.")

    # --- 3. Main Menu Loop ---
    while True:
        print("\n" + "="*50)
        print(f"[Current Universe: n={n}, c={c_vector}]")
        print("1: Single Orbit Investigation")
        print("2: Universal Range Scan (1–100)")
        print("q: Quit")
        mode = input("\nChoose a mode (1 / 2 / q): ")

        if mode.lower() == 'q':
            print("Closing the lab. Good work!")
            break

        if mode == '1':
            try:
                x_input = input("Enter initial value x: ")
                x = int(x_input)
                start_x = x
                seen = {x}
                history = [x]
                steps = 0
                max_value = x

                print(f"Tracking orbit: {start_x}")
                while True:
                    divided = False
                    for d in divisors:
                        if x % d == 0:
                            x //= d
                            divided = True
                            break

                    if not divided:
                        r = x % n
                        x = ((n + 1) * x + c_vector[r]) // n

                    if x > max_value:
                        max_value = x

                    steps += 1
                    if x == 1:
                        history.append(x)
                        print(f"Result: Converged to 1! (Steps: {steps}, Max: {max_value})")
                        break
                    if x in seen:
                        print(f"Result: Loop detected at {x} (Steps: {steps}, Max: {max_value})")
                        break
                    if x > 10**18:
                        print("Result: Diverged (exceeded limit).")
                        break
                    seen.add(x)
                    history.append(x)
            except ValueError:
                print("Please enter a valid number.")

        elif mode == '2':
            print("\nScanning from 1 to 100...")
            stats = {}
            for i in range(1, 101):
                curr = i
                path_seen = {curr}
                max_val = curr
                while curr != 1:
                    div = False
                    for d in divisors:
                        if curr % d == 0:
                            curr //= d
                            div = True
                            break
                    if not div:
                        r = curr % n
                        curr = ((n + 1) * curr + c_vector[r]) // n
                    if curr > max_val:
                        max_val = curr
                    if curr in path_seen:
                        break
                    path_seen.add(curr)

                res = f"Loop/Fixed at {curr}" if curr != 1 else "1 (Convergence)"
                stats[res] = stats.get(res, 0) + 1

            print("\n--- Scan Results (1–100) ---")
            for res_name, count in stats.items():
                print(f" {res_name}: {count} numbers")

# --- Entry Point ---
if __name__ == "__main__":
    n_adic_integrated_lab()


# In[ ]:




