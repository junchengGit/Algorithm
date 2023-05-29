import ford_fullkerson

graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5

#print(ford_fullkerson.maxflow_bfs(source,sink,graph))
print(ford_fullkerson.maxflow_dfs(source,sink,graph))
# Correct Work:
# >>> ford_fullkerson.maxflow_bfs(source,sink,graph)
# 23
# >>> ford_fullkerson.maxflow_dfs(source,sink,graph)
# 23
