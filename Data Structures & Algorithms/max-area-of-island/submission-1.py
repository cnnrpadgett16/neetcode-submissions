class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        def bfs(r, c):
            area = 1
            q = deque()
            visited.add((r, c))
            q.append((r,c))
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            while q:
              row, col = q.popleft() 
              for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and 
                    c in range(cols) and 
                    grid[r][c] == 1 and 
                    (r, c) not in visited):
                    area += 1
                    q.append((r, c)) 
                    visited.add((r , c))
            return max(max_area, area)

        for r in range(rows):
          for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
              max_area = bfs(r, c)
        return max_area
        '''
        1 0 0 1 1
        1 0 0 0 1
        1 1 0 1 0
        1 0 0 0 0
        
        max_area 
        
        visited = set()
        stack = [[i,j]] 


        for each grid position at row, column
            run a bfs(grid[row][col])


        '''

  


        