import math


def BFS(source: int,sink: int, graph: list, parents: list):
    """

    """
    # Mark all the vertices as not visited
    visited = [False]*len(graph)

    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(source)
    # Mean have already visited the Node
    visited[source] = True 

    #BSF loop
    while queue:

        # Dequeue a vertex from queue and print it
        u = queue.pop(0)

        for i,j in enumerate(graph[u]):
            if visited[i] == False and j > 0:
                queue.append(i)
                visited[i] = True
                parents[i] = u
                if i == sink:
                    return True
    return False
                

def maxflow_bfs(source: int,sink: int,graph: list):
    """

    """
    # This array use to store BFS and to store path
    parents = [-1]*len(graph)

    max_flow = 0 # There is no flow initially

    while BFS(source, sink, graph, parents):

        path_flow = math.inf
        s = sink
        while(s != source):
            if path_flow > graph[parents[s]][s]:
                path_flow = graph[parents[s]][s]
            s = parents[s]

    # Add path flow to overall flow
        max_flow +=  path_flow

        v = sink
        while(v!= source):
            u = parents[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parents[v]

    return max_flow

def DFS(source: int,sink: int, graph: list, parents: list, visited):
    """

    """
    # Mark all the vertices as not visited
    # Mean have already visited the Node
    visited[source] = True 
    #DSF loop
    for i, j in enumerate(graph[source]):
        if visited[i] == False and j > 0:
                visited[i] = True
                parents[i] = source
                if i == sink or DFS(i,sink,graph,parents,visited) == True:
                    return True            
    return False  
    

def maxflow_dfs(source: int,sink: int,graph: list):
    """

    """
    # This array use to store BFS and to store path
    parents = [-1]*len(graph)

    max_flow = 0 # There is no flow initially
    while DFS(source, sink, graph, parents,visited =[False]*len(graph)):

        path_flow = math.inf
        s = sink
        while(s != source):
            if path_flow > graph[parents[s]][s]:
                path_flow = graph[parents[s]][s]
            s = parents[s]

    # Add path flow to overall flow
        max_flow +=  path_flow

        v = sink
        while(v!= source):
            u = parents[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parents[v]
    return max_flow