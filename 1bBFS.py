graph={
'A':set(['B','C']),
'B':set(['A','D','E']),
'C':set(['A','F']),
'D':set(['B']),
'E':set(['B','F']),
'F':set(['C','E'])
}
def bfs(start):
     queue=[start]
     levels={}
     levels[start]=0
     visited=set(start)
     while queue:
         node=queue.pop(0)
         neighbours=graph[node]
         for neighbour in neighbours:
             if neighbour not in visited:
                 queue.append(neighbour)
                 visited.add(neighbour)
                 levels[neighbour] =levels[node]+1
     print(levels)
     return visited
print(str(bfs('A')))
def bfs_path(graph,start, goal):
     queue=[(start,[start])]
     while queue:
         (vertex,path)=queue.pop(0)
         for next in graph[vertex]-set(path):
             if next==goal:
                 yield path+[next]
             else:
                 queue.append((next,path+[next]))
result=list(bfs_path(graph,'A','F'))
print(result)






'''Breadth first search algorithm:
BFS stands for Breadth-First Search, which is another graph traversal algorithm used
to explore or search through a graph or tree data structure. Unlike DFS, which
explores the depth of a graph first, BFS explores the vertices at the same level before
moving to the next level.'''

