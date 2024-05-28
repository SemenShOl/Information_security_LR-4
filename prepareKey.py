
from typing import List
from P_BOXES import P_BOXES
from S_BOXES import S_BOXES
from utils import *
from crypto import encrypt


def setOpenKeyToRequiredSize(value: str, bitLength: int = 576) -> List[int]:
  requiredLength = int(bitLength / 8)
  expandedValue = value

  expandedKey = []

  while len(expandedValue.encode("utf-8")) < requiredLength:
    expandedValue += value

  expandedValue = expandedValue[:requiredLength]

  chunkSize = 4
  for i in range(0, len(expandedValue), chunkSize):
    chunk = expandedValue[i:i + chunkSize]
    expandedKey.append(stringToInt(chunk))

  return expandedKey


def setCloseKeyToRequiredSize(initialKey: List[int]) -> None:
  for i in range(18):
    P_BOXES[i] ^= initialKey[i]

  left, right = 0, 0
  for i in range(0, 18, 2):
    left, right = encrypt(left, right)
    P_BOXES[i] = left
    P_BOXES[i + 1] = right

  for i in range(4):
    for j in range(0, 256, 2):
      S_BOXES[i][j], S_BOXES[i][j + 1] = encrypt(S_BOXES[i][j], S_BOXES[i][j + 1])
