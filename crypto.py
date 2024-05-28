from P_BOXES import P_BOXES
from S_BOXES import S_BOXES
from typing import Tuple

def F(x: int) -> int:
  x %= (0x1 << 32)

  a = S_BOXES[0][x >> 24]
  b = S_BOXES[1][x >> 16 & 0xff]
  c = S_BOXES[2][x >> 8 & 0xff]
  d = S_BOXES[3][x & 0xff]

  return (a + b) ^ c + d

def encrypt(left: int, right: int) -> Tuple[int, int]:
  for i in range(16):
    left ^= P_BOXES[i]
    right ^= F(left)
    left, right = right, left

  left, right = right, left
  right ^= P_BOXES[16]
  left ^= P_BOXES[17]

  return [left, right]


def decrypt(left: int, right: int) -> Tuple[int, int]:
  for i in reversed(range(2, 18)):
    left ^= P_BOXES[i]
    right ^= F(left)
    left, right = right, left
  
  left, right = right, left
  left ^= P_BOXES[0]
  right ^= P_BOXES[1]

  return [left, right]
