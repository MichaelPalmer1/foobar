def answer(population, x, y, strength):
    if population[y][x] != -1 and population[y][x] <= strength:
        population[y][x] = -1

        # Up
        if y > 0:
            population = answer(population, x, y - 1, strength)

        # Down
        if y + 1 < len(population):
            population = answer(population, x, y + 1, strength)

        # Left
        if x > 0:
            population = answer(population, x - 1, y, strength)

        # Right
        if x + 1 < len(population[y]):
            population = answer(population, x + 1, y, strength)

    return population

p1 = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
x1 = 0
y1 = 0
s1 = 2
p1_answer = [[-1, -1, 3], [-1, 3, 4], [3, 2, 1]]

p2 = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
x2 = 2
y2 = 1
s2 = 5
p2_answer = [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]

print(answer(p1, x1, y1, s1))
assert (answer(p1, x1, y1, s1) == p1_answer)

print(answer(p2, x2, y2, s2))
assert (answer(p2, x2, y2, s2) == p2_answer)
