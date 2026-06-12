# BOJ 15829: 입력 a~z까지로 구성된 문자열 해시로 변경하기

class Hash:
    def main(self):
        while True:
            a_zstr = input('a~z로 구성된 문자열을 입력하세요(종료=0): ').lower()
            if a_zstr == '0':
                break
            else:
                print(self.hash(a_zstr))
        
    def hash(self, str):
        r = 31
        M = 1234567891
        alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        result = 0
        for i in range(len(str)):
            char = str[i]
            value = alpa.index(char) + 1
            result += value * (r ** i)
        return result % M
    
if __name__ == '__main__':
    app = Hash()
    app.main()