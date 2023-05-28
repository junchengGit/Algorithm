import ford_fullkerson

connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
(0, 3, 2000), (3, 4, 2000), (3, 2, 1000), (2,5,5000), (4,5, 5000)]
source = 0
sink = 5

print(ford_fullkerson.maxflow_bfs(source,sink,connections))
print(ford_fullkerson.maxflow_dfs(source,sink,connections))
# Correct Work:
# >>> maxThroughput(connections, maxIn, maxOut, origin, targets)
#4500

