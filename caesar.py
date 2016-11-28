import sys
def main():
    key=0
    text=""
    if len(sys.argv)!= 2:
        print("2 should be a command-line argument.Enter a non-negative integer.\n")                                                              
        return 1
    else:
      key = int(sys.argv[1])
      text = str(input("plaintext: "))
      print("ciphertext: ", sep='', end='')
      for i in range(len(text)):
          if text[i].isalpha():
            if text[i].islower():
               cipher = (ord(text[i]) - ord('a') + key) % 26 + ord('a')
               print(chr(cipher), end='')
            else:
               cipher = (ord(text[i]) - ord('A') + key) % 26 + ord('A')
               print(chr(cipher), end='')
          else:
            print(text[i], end='')
    print()
main()
      
