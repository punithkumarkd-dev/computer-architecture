
def rotate_left(value, positions):
    """Rotate an 8-bit number left without carry (ROL)."""
    mask = 0xFF
    value &= mask

    print("\n=== Rotate Left (ROL) ===")
    print(f"Original number : {value:08b}")

    for step in range(1, positions + 1):
        msb = (value >> 7) & 1
        value = ((value << 1) | msb) & mask
        print(f"Step {step}          : {value:08b}")

    print(f"Final binary    : {value:08b}")
    print(f"Final decimal   : {value}")


def rotate_left_carry(value, carry, positions):
    """Rotate an 8-bit number left through the carry flag (RCL)."""
    mask = 0xFF
    value &= mask

    print("\n=== Rotate Left through Carry (RCL) ===")
    print(f"Original binary : {value:08b}")
    print(f"Initial carry   : {carry}")

    for step in range(1, positions + 1):
        old_msb = (value >> 7) & 1
        value = ((value << 1) | carry) & mask
        carry = old_msb

        print(
            f"Step {step}          : {value:08b}, "
            f"Carry = {carry}"
        )

    print(f"Final binary    : {value:08b}")
    print(f"Final decimal   : {value}")
    print(f"Final carry     : {carry}")


# Given number and number of rotations
number = 0b10110110
positions = 2

rotate_left(number, positions)

# Assumption: initial carry flag is 0
rotate_left_carry(number, 0, positions)
