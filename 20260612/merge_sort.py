# 병합정렬 (Merge Sort)

class MergeSort:
    def main(self):
        num_list = []
        while True:
            try:
                input_num = int(input('정렬할 숫자 입력(입력종료=0): '))
            except ValueError:
                print('!!! 숫자만 입력하세요')
            else:
                if input_num == 0:
                    break
                num_list.append(input_num)
        self.merge_sort(num_list, 0, len(num_list) - 1)
        print(num_list)

    def merge_sort(self, A, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(A, left, mid)       # 왼쪽 절반 재귀
            self.merge_sort(A, mid+1, right)    # 오른쪽 절반 재귀
            self.merge(A, left, mid, right)     # 합치기

    def merge(self, A, left, mid, right):
        temp = [0] * len(A)
        k = left
        i = left
        j = mid + 1
        
        while i <= mid and j <= right:
            if A[i] <= A[j]:
                temp[k] = A[i]      # 왼쪽이 작으면 왼쪽 값 할당
                k, i = k+1, i+1
            else:
                temp[k] = A[j]      # 오른쪽이 작으면 오른쪽 값 할당
                k, j = k+1, j+1

        if i > mid:                             # 왼쪽 데이터 안남으면
            temp[k:k+right-j+1] = A[j:right+1]  # 오른쪽 남은 데이터 전체 복사
        else:
            temp[k:k+mid-i+1] = A[i:mid+1]
        A[left:right+1] = temp[left:right+1]    # temp[]에 반영

if __name__ == '__main__':
    app = MergeSort()
    # test_data = [27,10,12,20,25,13,15,22]
    # app.merge_sort(test_data, 0, len(test_data)-1)
    # print(test_data)
    app.main()