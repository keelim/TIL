class Solution(object):
    
    def bfs(self, grid):
        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]

        n = len(grid)
        visited = [[0]*101 for _ in range(101)]
        q = []
        q.append([0, 0, 1])
        visited[0][0] = 1

        while q:
            x, y, cnt = q.pop(0)

            if x == n-1 and y == n-1:
                return cnt

            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]

                if not(0<=nx<n and 0<=ny<n): continue

                if grid[nx][ny] == 0 and visited[nx][ny] == 0 :
                    q.append([nx, ny, cnt+11])
                    visited[nx][ny] = 1

        return -1

    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        elif grid[len(grid)-1][len(grid)-1] == 1:
            return -1

        return self.bfs(grid)
