#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing keys to 
    other boxes can be unlocked. The first box is always unlocked.
    '''

    num_boxes = len(boxes)
    unlocked_boxes = set([0])
    keys_to_use = list(boxes[0])

    while keys_to_use:
        current_key = keys_to_use.pop()

        if current_key not in unlocked_boxes and current_key < num_boxes:
            unlocked_boxes.add(current_key)
            keys_to_use.extend(boxes[current_key])

    return len(unlocked_boxes) == num_boxes
