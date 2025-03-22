cipher = "MFEVVUR"
wordList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = ""

for j in range(52):
    current_plaintext = ""
    for i in range(len(cipher)):
        if cipher[i] in wordList:
            shifted_index = (wordList.index(cipher[i]) - j) % 26
            current_plaintext += wordList[shifted_index]
        else:
            current_plaintext += cipher[i]

    print(f"Shift {j}: {current_plaintext}")
