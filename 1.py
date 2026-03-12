""" 1.Solving the 2-water jug Problem: Write a program to solve the 2-water jug problem by manually providing moves from the user. 2.Write a program to implement the Missionaries and Cannibals problem. Constraints: three missionaries and three cannibals must cross a river using a boat which can carry at most two people, under the constraint that, for both banks, if there are missionaries present on the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). The boat cannot cross the river by itself with no people on board."""

def water_jug():
    capA = int(input("Enter capacity of Jug A: "))
    capB = int(input("Enter capacity of Jug B: "))
    target = int(input("Enter target amount: "))

    A = 0
    B = 0

    while True:
        print("\nCurrent State -> A:", A, " B:", B)

        if A == target or B == target:
            print("Target achieved!")
            break

        print("""
Choose operation
1 Fill Jug A
2 Fill Jug B
3 Empty Jug A
4 Empty Jug B
5 Pour A -> B
6 Pour B -> A
7 Exit
""")

        choice = int(input("Enter choice: "))

        if choice == 1:
            A = capA

        elif choice == 2:
            B = capB

        elif choice == 3:
            A = 0

        elif choice == 4:
            B = 0

        elif choice == 5:
            transfer = min(A, capB - B)
            A -= transfer
            B += transfer

        elif choice == 6:
            transfer = min(B, capA - A)
            B -= transfer
            A += transfer

        elif choice == 7:
            break

        else:
            print("Invalid choice")

water_jug()



from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3-m) > 0 and (3-m) < (3-c):
        return False
    return True


def missionaries_cannibals():

    start = (3,3,1)
    goal = (0,0,0)

    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m,c,b), path = queue.popleft()

        if (m,c,b) == goal:
            print("Solution found:\n")
            for step in path:
                print(step)
            return

        for dm,dc in moves:

            if b == 1:
                new_state = (m-dm, c-dc, 0)
            else:
                new_state = (m+dm, c+dc, 1)

            if is_valid(new_state[0], new_state[1]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

missionaries_cannibals()
