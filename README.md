# 8-bit Rotate Left Simulator (ROL & RCL)

A small Python script that demonstrates, step by step, how two common assembly-language rotate instructions work on an 8-bit value:

- **ROL**: Rotate Left (without carry)
- **RCL**: Rotate Left through Carry

Each rotation is printed in binary so you can see exactly how the bits move.

## Requirements

- Python 3.6+ (uses f-strings)
- No external libraries

## Usage

1. Save the script as `rotate.py`.
2. Edit the inputs at the bottom of the file if needed:

   ```python
   number = 0b10110110   # 8-bit value to rotate
   positions = 2         # number of rotations

   rotate_left(number, positions)
   rotate_left_carry(number, 0, positions)   # 0 = initial carry flag
   ```

3. Run it:

   ```bash
   python rotate.py
   ```

## Functions

### `rotate_left(value, positions)`

Simulates **ROL**. On each step the most significant bit (MSB) is shifted out of the left end and re-inserted at the least significant bit (LSB). The carry flag is not involved.

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `value`     | The number to rotate (masked to 8 bits)  |
| `positions` | How many times to rotate left            |

### `rotate_left_carry(value, carry, positions)`

Simulates **RCL**. On each step the MSB moves into the carry flag, and the *old* carry value moves into the LSB. The carry flag is effectively a 9th bit in the rotation.

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `value`     | The number to rotate (masked to 8 bits)  |
| `carry`     | Initial carry flag (0 or 1)              |
| `positions` | How many times to rotate left            |

## How it works

| Operation | Per-step logic                                                         |
|-----------|------------------------------------------------------------------------|
| ROL       | `msb = value >> 7`; `value = ((value << 1) \| msb) & 0xFF`             |
| RCL       | `old_msb = value >> 7`; `value = ((value << 1) \| carry) & 0xFF`; `carry = old_msb` |

The `& 0xFF` mask keeps the result within 8 bits.

## Example

Input: `10110110` (decimal 182), rotated 2 positions, initial carry = 0.

```
=== Rotate Left (ROL) ===
Original number : 10110110
Step 1          : 01101101
Step 2          : 11011010
Final binary    : 11011010
Final decimal   : 218

=== Rotate Left through Carry (RCL) ===
Original binary : 10110110
Initial carry   : 0
Step 1          : 01101100, Carry = 1
Step 2          : 11011001, Carry = 0
Final binary    : 11011001
Final decimal   : 217
Final carry     : 0
```

## Notes

- The initial carry flag for RCL is assumed to be `0` in the example; change the second argument to test other cases.
- Input values larger than 8 bits are truncated to the lowest 8 bits.
- This is an educational simulation, not a hardware-accurate emulator (other CPU flags such as overflow are not modeled).
