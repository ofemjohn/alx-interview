def canUnlockAll(boxes):
    ''' Create a set to keep track of the boxes that have been visited'''
    visited = set()
    visited.add(0)
    '''# The first box is unlocked'''

    '''Create a queue to hold the boxes that need to be checked'''
    queue = [0]

    '''Loop through the queue and check the boxes'''
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in visited:
                visited.add(key)
                queue.append(key)

    '''If all the boxes have been visited, return True'''
    return len(visited) == len(boxes)
