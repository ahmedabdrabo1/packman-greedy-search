import numpy as np

N = 10
M = 10

number_of_pizzas = 5

packman_value = 11
pizza_value = 99

packman_position = np.random.randint(0, N, size=2)

pizza_positions = []

while len(pizza_positions) < number_of_pizzas:

    position = np.random.randint(0, N, size=2)

    if np.array_equal(position, packman_position):
        continue

    if list(position) in pizza_positions:
        continue

    pizza_positions.append(list(position))


game_board = np.zeros((N, M))

game_board[packman_position[0], packman_position[1]] = packman_value

for position in pizza_positions:
    game_board[position[0], position[1]] = pizza_value


print("Packman Position:")
print(packman_position)

print("\nPizza Positions:")
print(pizza_positions)

print("\nGame Board:")
print(game_board)


def get_possible_moves(position):

    possible_moves = []

    row = position[0]
    column = position[1]

    if row - 1 >= 0:
        possible_moves.append([row - 1, column])

    if row + 1 < N:
        possible_moves.append([row + 1, column])

    if column - 1 >= 0:
        possible_moves.append([row, column - 1])

    if column + 1 < M:
        possible_moves.append([row, column + 1])

    return possible_moves


def calculate_distances(current_position, target_positions):

    current_position = np.array(current_position)

    distances = []

    for target_position in target_positions:

        target_position = np.array(target_position)

        distance = np.abs(current_position - target_position).sum()

        distances.append(distance)

    return distances


def get_nearest_pizza(position):

    distances = calculate_distances(
        position,
        pizza_positions
    )

    nearest_index = np.argmin(distances)

    return pizza_positions[nearest_index]


def game(position):

    eaten_pizzas = 0

    while pizza_positions:

        possible_moves = get_possible_moves(position)

        target_pizza = get_nearest_pizza(position)

        move_distances = calculate_distances(
            target_pizza,
            possible_moves
        )

        best_move_index = np.argmin(move_distances)

        next_position = possible_moves[best_move_index]

        game_board[position[0], position[1]] = 0

        game_board[next_position[0], next_position[1]] = packman_value

        position = next_position

        if position in pizza_positions:

            eaten_pizzas += 1

            pizza_positions.remove(position)

            print("\nPizza Eaten!")

        print("\nPackman Position:")
        print(position)

        print("\nTarget Pizza:")
        print(target_pizza)

        print("\nGame Board:")
        print(game_board)

        print("\nPizzas Left:")
        print(pizza_positions)

        print("\nEaten Pizzas:")
        print(eaten_pizzas)


game(packman_position)
