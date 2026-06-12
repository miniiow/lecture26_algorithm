# BOJ 1181: 단어정렬

class BOJ1181:
    def main(self):
        words = []
        try:
            turn = int(input('입력횟수 정수로 입력: '))
        except ValueError:
            print('!!! 정수로 입력하세요')
        else:
            words = []
            for _ in range(turn):
                 words.append(input('단어입력: '))
            words = self.char_sort(words)
            for word in words:
                print(word)

    def char_sort(self, words):
        words.sort(key=lambda x: (len(x), x))
        return words

if __name__ == '__main__':
    app = BOJ1181()
    app.main()