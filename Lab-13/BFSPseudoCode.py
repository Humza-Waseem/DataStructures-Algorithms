def BFS(g,root,goal):
    queue = []    # Making a queue
    discovered = []    # Making a list for discovered nodes
    queue.append(root)   # first we add the root node(Vertex) to the queue 
    discovered.append(root)   # adding the root node to the discovered list, It is now discovered so we don't need to discover it again ,,, we will look for its edges now

    while len(queue) > 0:   # we check if the queue is empty or not,,, if empty then we have discovered all the nodes,,, otheerwise we will continue to discover nodes and add them to the queue,,,,,, 
        # in the first case the root node has been discovered and added to the queue, so we will look for its edges and add them to the queue and discovered list   in the (step1 below)
        
        v = queue.pop()    # we pop the first node in the queue and assign it to v

        if(v == goal):   # if we want to search for a certain node that is Goal,, and if it is found then we return v
            return v
        for u in g[v]:   # Step1: we look for the edges of the node v and add them to the queue and discovered list
            if u not in discovered:
                queue.append(u)
                discovered.append(u)
    return discovered
    

