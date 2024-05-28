from typing import List, Tuple
from sys import argv

from P_BOXES import P_BOXES
from S_BOXES import S_BOXES
from utils import *
from crypto import encrypt, decrypt
from prepareKey import setOpenKeyToRequiredSize, setCloseKeyToRequiredSize
from prepareMessage import prepareMessage, extractMessage



def main():
  openKey = input("Введите ключ: ")
  expandedOpenKey = setOpenKeyToRequiredSize(openKey)
  setCloseKeyToRequiredSize(expandedOpenKey)

  message = input("Введите сообщение: ")
  countOfExtraChars, preparedMessage = prepareMessage(message)

  encryptedMessage = []

  for i in preparedMessage:
    encryptedMessage.append(encrypt(*getPair(i)))

  print("Зашифрованное сообщение:", *encryptedMessage, sep=" ")

  decryptedMessage = []
  for i in encryptedMessage:
    left, right = decrypt(i[0], i[1])
    decryptedMessage.append([left, right])

  print("Расшифрованное сообщение:", extractMessage(decryptedMessage, countOfExtraChars), sep=" ")


main()