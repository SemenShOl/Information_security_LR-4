
from typing import List
from utils import *


def prepareMessage(message: str) -> Tuple[int, List[Tuple[int, int]]]:
  countOfExtraChars = 8 - len(message) % 8
  message += countOfExtraChars * "0"

  chunkSize = 8
  messageArr = [message[i:i + chunkSize] for i in range(0, len(message), chunkSize)]
  return countOfExtraChars, messageArr


def extractMessage(decryptedMessage: List[Tuple[int, int]], countOfExtraChars: int) -> str:
  extractedMessage = ""

  for i in decryptedMessage:
    for j in i:
      extractedMessage += intToString(j)

  return extractedMessage[:-countOfExtraChars]