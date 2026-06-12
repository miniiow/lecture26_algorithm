# BOJ 11650: 좌표 정렬하기

class BOJ11650:
    def main(self):
        try:
            dot = int(input('점 개수 입력: '))
        except ValueError:
            print('!!! 숫자로 입력하세요')
        else:
            coords = []
            for _ in range(dot):
                coord = (input('좌표입력: ')).split()
                a = (int(coord[0]), int(coord[1]))
                coords.append(a)
        self.coordinate_sort(coords)
        for coord in coords:
            print(coord[0], coord[1])

    def coordinate_sort(self, coords):
        coords.sort(key=lambda x: (x[0], x[1]))
        return coords
    
if __name__ == '__main__':
    app = BOJ11650()
    app.main()