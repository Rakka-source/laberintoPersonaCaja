from Reversso_Felipe_Gutierrez import *
# grid= ["#####",
#         "###D#",
#         "###.#",
#         "###.#",
#         "#P..#",
#         "#####"]

# grid= [ [".",".",".","#","#"],
#         ["P","C",".","D","#"],
#         [".",".",".","#","#"]]

###**** Complicado

# grid= [["#","#","#",".","."], 
#         ["#","#","#",".","#"],
#         ["#","#",".",".","#"],
#         [".",".",".",".","."],
#         ["P","#","C","#","#"],
#         [".",".",".","D","#"]]

# grid = [["#","#","#","#","#"],
#         ["#","#","#","D","#"],
#         ["#","#","#",".","#"],
#         ["#","#","#",".","#"],
#         ["#","P",".","C","#"],
#         ["#","#","#","#","#"]]
# grid= [["#","#","#",".","."],
#         ["#","#","#",".","#"],
#         ["#","#","C",".","#"],
#         [".",".",".",".","#"],
#         ["P","#","D","#","#"],
#         [".",".",".",".","#"]]


###*** __FIN COMPLICADO__

grid= [["#","#","#",".","."],
        ["#","P",".","D","#"],
        ["#","#","C","#","#"],
        ["#",".",".",".","#"],
        ["#",".","#",".","#"],
        ["#",".",".",".","#"]]

[(3, 4), (3, 3), (2, 3), (2, 2)]

print(search_path(grid))