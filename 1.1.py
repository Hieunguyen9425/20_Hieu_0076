#Bài tập 1.1
characters = {
    'h': ["**  **", "**  **", "******", "**  **", "**  **"],
    'e': ["******", "**    ", "******", "**    ", "******"],
    'l': ["**    ", "**    ", "**    ", "**    ", "******"],
    'o': [" ****** ", " **  **", " **  **", " **  **", " ****** "]
}
text = "hello"
for row in range(5):
    for char in text:
        print(characters[char][row], end="  ") 
    print() 