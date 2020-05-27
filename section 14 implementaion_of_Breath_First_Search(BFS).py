def breath_first_search(binary_tree,vertex):
    visited_vertex = [] #list to keep track of visited vertesies
    queue = [] #queue to keep track of all the sub trees/child nodes of the tree.
    queue.append(binary_tree)
    while queue:
        #adding sub tree to the queue
        binary_tree = queue.pop(0)
        #adding the tree value to the visited_vertex list
        visited_vertex.append(binary_tree['value'])
        if visited_vertex[-1]==vertex:
            print('vertex is found!')
            break
        #if left child node exists then add it to the queue
        if binary_tree['low']:
            queue.append(binary_tree['low'])
        #if right child node exists then add it to the queue
        if binary_tree['high']:
            queue.append(binary_tree['high'])
    return visited_vertex



#test
#tree of the graph should look like this
#      9
#    /   \
#   4     20
#  /  \   /  \
# 1    6  15  200

graph = {'value': 9, 'high': {'value': 20, 'high': {'value': 200, 'high': None, 'low': None}, 'low': {'value': 15, 'high': None, 'low': None}}, 'low': {'value': 4, 'high': {'value': 6, 'high': None, 'low': None}, 'low': {'value': 1, 'high': None, 'low': None}}}
vertex = 200
breath_first_search(graph,vertex)