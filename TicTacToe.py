while True:
    cells = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    print(f"""
    ---------
    | {cells[0]} {cells[1]} {cells[2]} |
    | {cells[3]} {cells[4]} {cells[5]} |
    | {cells[6]} {cells[7]} {cells[8]} |
    ---------""")

    a = "1 1"
    b = "1 2"
    c = "1 3"
    d = "2 1"
    e = "2 2"
    f = "2 3"
    g = "3 1"
    h = "3 2"
    i = "3 3"

    scores = []


    while True:
        while True:
            while True:
                coordinates = input("Enter the coordinates: ")

                possible_moves = [a, b, c, d, e, f, g, h, i]
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

            if coordinates == a:
                if cells[0] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[0] = "X"
                    added = cells[0]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == b:
                if cells[1] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[1] = "X"
                    added = cells[1]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == c:
                if cells[2] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[2] = "X"
                    added = cells[2]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == d:
                if cells[3] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[3] = "X"
                    added = cells[3]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == e:
                if cells[4] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[4] = "X"
                    added = cells[4]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == f:
                if cells[5] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[5] = "X"
                    added = cells[5]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == g:
                if cells[6] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[6] = "X"
                    added = cells[6]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == h:
                if cells[7] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[7] = "X"
                    added = cells[7]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == i:
                if cells[8] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[8] = "X"
                    added = cells[8]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            continue

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


        while True:
            while True:
                coordinates = input("Enter the coordinates: ")

                possible_moves = [a, b, c, d, e, f, g, h, i]
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

            if coordinates == a:
                if cells[0] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[0] = "O"
                    added = cells[0]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == b:
                if cells[1] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[1] = "O"
                    added = cells[1]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == c:
                if cells[2] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[2] = "O"
                    added = cells[2]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == d:
                if cells[3] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[3] = "O"
                    added = cells[3]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == e:
                if cells[4] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[4] = "O"
                    added = cells[4]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == f:
                if cells[5] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[5] = "O"
                    added = cells[5]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == g:
                if cells[6] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[6] = "O"
                    added = cells[6]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == h:
                if cells[7] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[7] = "O"
                    added = cells[7]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            if coordinates == i:
                if cells[8] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[8] = "O"
                    added = cells[8]
                    print(f"""
                    ---------
                    | {cells[0]} {cells[1]} {cells[2]} |
                    | {cells[3]} {cells[4]} {cells[5]} |
                    | {cells[6]} {cells[7]} {cells[8]} |
                    ---------""")
                    break
            continue

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
        continue
    again = input("Do you want to play again?  (yes/no)\n")
    if again == "yes":
        continue
    else:
        print("See you next time!")
        break

