class Solution:
    def calc_sum(self, i, j, size, grid) -> int:
        if size == 0 or (i + size*2+1) > len(grid): 
            return grid[i][j]
        
        sum = 0
        for x in range(size+1):
            sum+= grid[i+x][j-x]
            sum+= grid[i+x][j+x]
            sum+= grid[i+size+x][j-x]
            sum+= grid[i+size+x][j+x]
            
        sum -= (grid[i][j] + grid[i+size][j-size] + grid[i+size*2][j] + grid[i+size][j+size])
        return sum
    
    def getBiggestThree(self, grid: [[int]]) -> [int]:
        res = []
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                possible_size = min(j+1, m-j)
                for size in range(possible_size):
                    sum = self.calc_sum(i,j,size,grid)
                    if sum not in res:
                        res.append(sum)
                        if len(res) > 3:
                            res.sort(reverse=True)
                            res.pop()
        
        
        return sorted(res, reverse=True)

i = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
print(Solution().getBiggestThree(i))

