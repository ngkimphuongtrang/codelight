# each move, Bastian can go in 4 directions: up, down, left, right
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

def onBoard(x, y):
  """Return True if the coordinate is still on the map"""
  global m, n 
  return 0 <= x < m and 0 <= y < n

def Hamilton(x, y):
  """Backtracking all possible ways of Hamilton paths, result[] saves the paths"""
  global path, places,t, graph,  visited, result
  if len(path) == places:
    des = path[-1]
    if des == t:
      result.append(path.copy())
    return 
  for i in range(4):
    xx = dx[i] + x 
    yy = dy[i] + y 
    if onBoard(xx,yy) and visited[xx][yy] == False and graph[xx][yy] != 1:
      path.append([xx,yy])
      visited[xx][yy] = True 
      Hamilton(xx, yy)
      visited[xx][yy] = False 
      path.pop()

m, n = map(int, input().split())
graph = []
for i in range(m):
  l = list(map(int, input().split()))
  graph.append(l)
visited = [[False]*n for _ in range(m)]
result = []
src = [-1,-1] #source
t = [-1, -1] # destination
places = 2 # number of places need to be visited, 2 for source, destination places.
# print(graph)
for i in range(m):
  for j in range(n):
    if graph[i][j] == 2:
      src = [i,j]
    elif graph[i][j] == 3:
      t = [i,j]
    elif graph[i][j] == 0:
      places += 1

path = []
visited[src[0]][src[1]] = True 
path.append(src)
Hamilton(src[0], src[1])
print(len(result))
# O(4^(m*n))
