# 8-bit Signed Addition and Subtraction (Two's Complement)

A Python script that solves two questions using **8-bit two's complement** arithmetic and reports the binary result, the signed decimal result, and whether **overflow** occurred.

| Question | Expression        |
|----------|-------------------|
| Q1(a)    | 34 + (+27)        |
| Q1(b)    | (-34) - (-27)     |

## Requirements

- Python 3.6+
- No external libraries

## Usage

```bash
python signed_arithmetic.py
```

Edit the values of `a` and `b` in the script to test other inputs.

## Background

- **Range of 8-bit signed numbers:** -128 to +127.
- **Two's complement:** a negative number is stored as `256 - |n|`, i.e. invert the bits of the positive value and add 1.
- **Subtraction:** `A - B` is computed as `A + (-B)`, so the same adder handles both operations.
- **Overflow:** occurs when the true result falls outside -128 to +127 (equivalently, when the carry into the sign bit differs from the carry out of it).

## Functions

### `binary_8bit(n)`
Returns `n` as an 8-character binary string. `n & 0xFF` keeps only the lowest 8 bits, which converts negative numbers to their two's complement form.

### `signed_value(n)`
Interprets an 8-bit pattern as a signed number. If the sign bit (`0x80`) is set, it returns `n - 256`; otherwise it returns `n`.

### `add_8bit(a, b)`
Adds two numbers and returns `(result, overflow)`:
- `result = (a + b) & 0xFF` is the 8-bit wrapped sum.
- `overflow` is `True` if `a + b` is outside -128 to +127.

## Q1(a): 34 + (+27)

**Step 1: Convert to 8-bit binary**

- `34 = 00100010`
- `+27 = 00011011`

**Step 2: Add**

```
  00100010   (34)
+ 00011011   (27)
----------
  00111101   (61)
```

**Step 3: Check overflow**

Both operands are positive and the result (61) is within -128 to +127, so there is **no overflow**.

| Result Binary | Result Decimal | Overflow |
|---------------|----------------|----------|
| `00111101`    | 61             | False    |

## Q1(b): (-34) - (-27)

**Step 1: Convert to 8-bit two's complement**

- `34 = 00100010` → invert → `11011101` → add 1 → `-34 = 11011110`
- `27 = 00011011` → invert → `11100100` → add 1 → `-27 = 11100101`

**Step 2: Turn subtraction into addition**

`(-34) - (-27) = (-34) + (+27)`

The script does this with `add_8bit(a, -b)`.

**Step 3: Add**

```
  11011110   (-34)
+ 00011011   (+27)
----------
  11111001   (-7)
```

**Step 4: Check overflow**

Adding a negative and a positive number can never overflow, and the result (-7) is within range, so there is **no overflow**.

**Step 5: Read the signed value**

`11111001` has the sign bit set, so its value is `249 - 256 = -7`.

| Result Binary | Result Decimal | Overflow |
|---------------|----------------|----------|
| `11111001`    | -7             | False    |

## Expected Output

```
Q1(a): 34 + (+27)
34  = 00100010
+27 = 00011011
Result Binary : 00111101
Result Decimal: 61
Overflow      : False

Q1(b): (-34) - (-27)
-34 = 11011110
-27 = 11100101
Result Binary : 11111001
Result Decimal: -7
Overflow      : False
```

## Summary

| Question | Operation       | Binary Result | Decimal | Overflow |
|----------|-----------------|---------------|---------|----------|
| Q1(a)    | 34 + 27         | `00111101`    | 61      | No       |
| Q1(b)    | (-34) - (-27)   | `11111001`    | -7      | No       |

## Notes

- The `-27 =` line in Q1(b) shows the binary of -27 as stored, while the calculation uses `-b` (+27) to perform the subtraction.
- The overflow check uses the true mathematical sum, which is simple and correct for 8-bit signed values.
- This is an educational simulation, not a full CPU emulator (carry, zero, and sign flags are not modeled).








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
