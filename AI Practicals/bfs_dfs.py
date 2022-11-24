# Creating Graph for BFS and DFS Searching

graph = {
    '5' : ['1'],
    '1' : ['2','3','5'],
    '2' : ['1','4'],
    '3' : ['1','4'],
    '4' : ['3','2']
}

#DFS
visited_DFS =[]

# define DFS function
def dfs(visited_list, graph, node):
    if node not in visited_list:
        print(node, end=" ")
        visited_list.append(node)
        for neighbour in graph[node]:
            dfs(visited_list, graph, neighbour)

#BFS
visited_BFS = []
queue = []

#defining function for BFS Search
def bfs(visited_list, graph,node):
    visited_list.append(node)
    queue.append(node)

    while queue:
        front = queue.pop(0)
        print(front, end=" ")

        for neighbour in graph[front]: 
            if neighbour not in visited_list:
                visited_list.append(neighbour)
                queue.append(neighbour)

#Driver Code
print("Following is the Depth First Search:")
dfs(visited_DFS, graph, '5')
print(" ")
print("Following is the Breadth First Search:")
bfs(visited_BFS, graph, '5')