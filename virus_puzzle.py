#!/usr/bin/env python

import copy
import sys

def printf(format,*args): sys.stdout.write(format%args)

(RIGHT, UP, LEFT, DOWN) = (0,1,2,3)

def east(i):
    return i + 1 if i % 4 < 3 else None

def north(i):
    return i - 4 if i / 4 > 0 else None
    
def west(i):
    return i - 1 if i % 4 > 0 else None

def south(i):
    return i + 4 if i / 4 < 3 else None

def build_new_lab():
    paths = []
    destroyed_rooms = []
    for i in xrange(0, 16):
        destroyed_rooms.append(False)

    for i in xrange(0,16):
        doors = [] #  [east, north, west, south]
        doors.append(east(i))
        doors.append(north(i))
        doors.append(west(i))
        doors.append(south(i))
        paths.append(doors)
        destroyed_rooms.append(False)
    return (paths, destroyed_rooms)

def destroy_room(paths, room_id):
    #destroy all doors in this room
    paths[room_id] = [ None, None, None, None]

    #Destroy all doors in other rooms leading here
    if east(room_id):
        paths[east(room_id)][0] = None
    if north(room_id):
        paths[north(room_id)][1] = None
    if west(room_id):
        paths[west(room_id)][2] = None
    if south(room_id):
        paths[south(room_id)][3] = None

def copy_paths(paths):
    new_paths = []
    for room in paths:
        new_room = room[:]
        new_paths.append(new_room)
    return new_paths

def search_exit(paths, trail, destroyed, room_id):
    trail.append(room_id)
    if room_id == 15:
        printf("EXIT trail is %s ", trail)
        if len(trail) >= 16:
            printf(" SOLUTION\n")
        else:
            printf(" MISS\n")

    for direction in (east, north, west, south):
        n = direction(room_id)
        if n is not None and not destroyed[n]:
            new_paths = copy_paths(paths)
            new_trail = trail[:]
            new_destroyed = destroyed[:]
            destroy_room(new_paths,n) # Make sure we can't come back
            new_destroyed[n] = True
            search_exit(new_paths, new_trail, new_destroyed, n)

(lab, destroyed) = build_new_lab()
trail = []
search_exit(lab, trail, destroyed, 0)
