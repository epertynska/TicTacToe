cells = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

print(f"""
---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
---------""")

signx = "X"
signo = "O"
possible_combinations = ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1", "3 2", "3 3"]
scores = []

i = 0
while i < 10:
    if i % 2 == 0:
        sign = signx
    elif i % 2 == 1:
        sign = signo
    while True:
        coordinates = input("Enter the coordinates: ")
        separate_coordinates = coordinates.split()
        try:
            big_int_coordinates = [int(x) for x in separate_coordinates if int(x) < 1 or 3 < int(x)]
            if any(big_int_coordinates):
                print("Coordinates should be from 1 to 3!")
            else:
                break
        except:
            print("You should enter numbers!")
        continue
    if coordinates in possible_combinations:
        if cells[possible_combinations.index(coordinates)] != "_":
            print("This cell is occupied! Choose another one!")
        else:
            cells[possible_combinations.index(coordinates)] = sign
            added = sign
            grid = f"""
            ---------
            | {cells[0]} {cells[1]} {cells[2]} |
            | {cells[3]} {cells[4]} {cells[5]} |
            | {cells[6]} {cells[7]} {cells[8]} |
            ---------"""
            print(grid)
            i += 1
    ctrl_o = [o for o in cells if o == "O"]
    ctrl_x = [x for x in cells if x == "X"]
    ctrl_draw = [d for d in cells if d != "_"]
    if (cells[0] == cells[1] == cells[2] != "_") or (cells[3] == cells[4] == cells[5] != "_") or (cells[6] == cells[7] == cells[8] != "_") or (cells[0] == cells[3] == cells[6] != "_") or (cells[1] == cells[4] == cells[7] != "_") or (cells[2] == cells[5] == cells[8] != "_") or (cells[0] == cells[4] == cells[8] != "_") or (cells[2] == cells[4] == cells[6] != "_"):
        scores.append(added)
  
    impossible = (len(ctrl_o) - len(ctrl_x)) > 1 or (len(ctrl_x) - len(ctrl_o) > 1) or (len(scores) > 1)
    win = len(scores) == 1
    draw = len(scores) == 0 and len(ctrl_draw) == 9
    not_finished = len(scores) == 0 and len(ctrl_draw) < 9 and not impossible

    if impossible:
        print("Impossible")
    elif win:
        print(f"{added} wins")
        break
    elif not_finished:
        print("Game not finished")
    elif draw:
        print("Draw")
        break
