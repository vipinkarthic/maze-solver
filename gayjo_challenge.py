from PIL import Image
import time
import sys

sys.setrecursionlimit(10**6)

start_time = time.time()

maze = Image.open(r"D:\Coding\My Stupidity Palace\PYTHON\Arbitrary Codes\frames\frame_0.png")
maze = maze.convert("L")

print(f"Image Size: {maze.size}")

#================================================================================================
#=================================== Mapping Starts here ========================================
#================================================================================================
maze_2d: list[list[int]] = [[]]

#----------------------------------------------------------
#Making stupid python lists in to c style array for usage easiness
#----------------------------------------------------------
for i in range(maze.height):
    maze_2d.append([])
    for j in range(maze.width):
        maze_2d[i].append(0)

#----------------------------------------------------------
#------------------Mapping Maze Pixels----------------------
#----------------------------------------------------------
for i in range(maze.height):
    for j in range(maze.width):
        maze_2d[i][j] = maze.getpixel((j, i))


for i in range(len(maze_2d)):
    for j in range(len(maze_2d[i])):
        #White as 0s and Black as 1s
        if maze_2d[i][j] == 255:
            maze_2d[i][j] = 0
        else:
            maze_2d[i][j] = 1

#----------------------------------------------------------
#------------------Printing the Maze-----------------------
#----------------------------------------------------------
maze_2d = maze_2d[0:5769]
for i in range(len(maze_2d)):
    print(maze_2d[i])

#================================================================================================
#=================================== Mapping Ends here ==========================================
#================================================================================================



#================================================================================================
#=================================== Solving Starts here ========================================
#================================================================================================
# Defining Start and end coordinates
# Size is pretty much 40x40
x_start, y_start = 1, 0
x_end, y_end = 5767, 5768

#Treat y_start as x and x_start as y

print(f"Start: {x_start}, {y_start}")
print(maze_2d[y_start][x_start])
print(f"End: {x_end}, {y_end}")
print(maze_2d[y_end][x_end])

# Making a visited bool 2d_matrix
visited = []
for i in range(len(maze_2d)):
    visited.append([])
    for j in range(len(maze_2d[i])):
        visited[i].append(False)

# Storing the Answer Path here
list_of_all_paths = []

def solve_maze(x, y, path=[]):
    # Checking if its a wall or a if its reached the boundary
    if x > len(maze_2d[0]) or y > len(maze_2d) or x < 0 or y < 0 or maze_2d[y][x] == 1:
        return False

    # CHecking if its already visited
    if visited[y][x]:
        return False

    # Adding it to the solution
    path.append((x, y))

    # Checking if its the end
    if x == x_end and y == y_end:
        list_of_all_paths.append(path.copy())
        path.pop()
        return True

    # Marking it as visited
    visited[y][x] = True

    # Checking for all the possible directions 
    up = solve_maze(x, y-1, path)
    down = solve_maze(x, y+1, path)
    left = solve_maze(x-1, y, path)
    right = solve_maze(x+1, y, path)

    #If it comes to this point, it means that the path is not correct
    # So remarking the point as False and popping it from the path
    visited[y][x] = False
    path.pop()
    return False

solve_maze(x_start, y_start)


for path in list_of_all_paths:
    print(path)

#================================================================================================
#=============================SOLUTION MAPPING THE MAZE (IMAGE)==================================
#================================================================================================

print(len(list_of_all_paths))
print(len(list_of_all_paths[0]))

# Creating a plain white image
solution = Image.new("RGB", (maze.width, maze.height), "white")

maze = maze.convert("RGB")
for coords in list_of_all_paths[0]:
    maze.putpixel(coords, (255, 0, 0))

maze.save(r"D:\Coding\My Stupidity Palace\PYTHON\Arbitrary Codes\alex_solved_final.png") 


#----------------------------------------------------------
#------------Time Taken to Execute the Code----------------
#----------------------------------------------------------
print(f"Time Taken: {time.time() - start_time} seconds")

