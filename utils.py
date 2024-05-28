from typing import Tuple

def stringToInt(value: str) -> int:
  byte_value = value.encode()
  return int.from_bytes(byte_value, byteorder="big")


def intToString(value: int) -> str:
  byte_value = value.to_bytes((value.bit_length() + 7) // 8, byteorder="big")
  return byte_value.decode("utf-8")


def getPair(value: str) -> Tuple[str, int]:
  return stringToInt(value[:4]), stringToInt(value[4:])
