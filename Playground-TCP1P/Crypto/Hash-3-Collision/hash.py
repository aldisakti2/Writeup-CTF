def my_hash(string):
    sum = 0
    for char in string:
        sum += ord(char)
    sum = sum % 2**24
    return str(sum).encode().hex()

def find_collision(target_sum, max_length=8):
    from collections import deque

    ascii_printable = list(range(32, 127))  # Printable ASCII characters
    queue = deque([''])

    while queue:
        current_string = queue.popleft()
        current_sum = sum(ord(char) for char in current_string) % (2**24)

        if current_sum == target_sum and current_string != '':
            print(current_string)
            return current_string

        if len(current_string) < max_length:
            for ascii_val in ascii_printable:
                queue.append(current_string + chr(ascii_val))

    return None

target_hex = '32323931'
target_sum = int(target_hex, 16)

collision_string = find_collision(target_sum)
if collision_string:
    print(f"Collision string for target hash {target_hex}: {collision_string}")
else:
    print("No collision string found within the given length.")

if collision_string:
    collision_hash = my_hash(collision_string)
    print(f"Hash of collision string: {collision_hash}")
    assert collision_hash == target_hex, "Hash does not match!"
    print("Collision verified successfully!")

