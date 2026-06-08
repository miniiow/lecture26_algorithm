from collections import deque
class Graph:
    def __init__(self, bidirection = True):
        num_nodes, num_edges = map(int, input().split())
        self.directed = int(input('양방향여부 (1:양방향/0:단방향) : '))
        self.graph = [[] for _ in range(num_nodes+1)]
        for _ in range(num_edges):
            # u: 부모노드, v: 자식노드
            u, v = map(int, input().split())
            self.graph[u].append(v) # graph[u]에 v할당
            # bidirection 값이 
            if bidirection:
                self.graph[v].append(u)
        # 방문한 node 리스트로 관리
        self.visited = []
    
    def dfs(self, node):
        self.visited.append(node)
        print(node, end=' ')
        # self.visited.append(node)
        for adj_node in self.graph[node]:
            # 방문하지 않은 node만 재귀함수로 진행
            if adj_node not in self.visited:
                self.dfs(adj_node)

    def bfs(self, start):
        self.visited.clear()
        queue = deque()
        # 시작 노드에 대해 작업
        queue.append(start)
        self.visited.append(start)
        print(start, end=' ')
        # 다음에 방문할 노드(= 방문한 적이 없고 인접노드를 찾을 노드) 찾아서 처리
        # 방문한 노드를 찾을 노드를 queue에서 가져와서 찾기
        while queue:
            # prev_node : 이미 방문한 노드
            prev_node = queue.popleft()
            for node in self.graph[prev_node]:
                if node not in self.visited:
                    queue.append(node)
                    self.visited.append(node)
                    print(node, end=' ')
                


if __name__ == '__main__':
    g = Graph(bidirection=False)
    start = int(input('시작 노드 번호 입력 : '))
    g.dfs(start)
    print()
    g.visited = []
    g.bfs(start)
    print()