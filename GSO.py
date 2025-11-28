import random
import numpy

# result after completing optimization process
class Result:
    def __init__(self):
        self.leader_fitness = 0
        self.leader_solution = 0
        self.func_evals = 0

"""
LCO = Leaders-Chain-Optimizer
Each individuals considers higher fitter individual as his leader.
So, it moves towards higher fitter individual.
"""
def LCO(fitness_func, sol_count, dimensions, iterations_count,
        lower_bound, upper_bound, mutation_rate=0.5,
        stopping_func=None, plt_func=None, verbose=True):

    # initialize position, fitness of leader solution
    #leader_fitness = float("inf")

    # convert lower_bound, upper_bound to array
    if not isinstance(lower_bound, list):
         lower_bound = [lower_bound for _ in range(dimensions)]
         upper_bound = [upper_bound for _ in range(dimensions)]

    # initialize solutions
    solutions = []
    solutions_fitness = [float("inf") for _ in range(sol_count)]

    for s in range(sol_count):
        sol = []
        for d in range(dimensions):
            d_val = random.uniform(lower_bound[d], upper_bound[d])
            sol.append(d_val)

        solutions.append(sol)

    solutions = numpy.array(solutions)

    # initialize result
    result = Result()

    # current iteration
    t = 0
    while t < iterations_count:
        # calculate fitness of individuals
        for s in range(0, sol_count):
            # clip solutions outside range
            for d in range(dimensions):
                sd = solutions[s, d]
                if sd > upper_bound[d]:
                    solutions[s, d] = upper_bound[d]
                elif sd < lower_bound[d]:
                    solutions[s, d] = lower_bound[d]

            #solutions[s, :] = numpy.clip(solutions[s, :], lower_bound, upper_bound)

            solutions_fitness[s] = fitness_func(solutions[s, :])
            result.func_evals += 1

        # sort population based on fitness value
        solutions = solutions[numpy.array(solutions_fitness).argsort()]
        solutions_fitness = sorted(solutions_fitness)

        leader_fitness = solutions_fitness[0]

        # should optimization process stop?
        if stopping_func is not None and stopping_func(leader_fitness, solutions[0], t):
            break

        if plt_func is not None:
            plt_func(t, leader_fitness)

        # loop from lower-fitness to higher
        # from index (sol_count - 1) to index 1
        # leader will not be effected [Elitism]
        A = 1 - 1 * t / iterations_count

        for s in range(sol_count - 1, 0, -1):
            m = random.uniform(0, 1)

            rs = random.sample(range(sol_count), 3)
            rs1, rs2, rs3 = sorted(rs)

            for d in range(dimensions):
                if mutation_rate > m and s > 0.5 * sol_count:
                    # good for benchmark functions
                    chain_index = (rs1) / sol_count
                    led_d = (leader_fitness / solutions_fitness[s])
                    nLed_d = (solutions_fitness[rs2] / solutions_fitness[rs3])
                    solutions[s, d] = chain_index * solutions[rs1, d] + A * (led_d + nLed_d)
                else:
                    # move effected by chain-leader, nearest-neighbour
                    # good for constrained engineering problems
                    sd = solutions[s, d]
                    d_gLeader = (solutions[0, d] - sd)
                    d_mLeader = (solutions[s - 1, d] - sd)

                    solutions[s, d] = sd + A * (d_gLeader + d_mLeader)

        if verbose and t % 10 == 0:
            log_txt = 'Iter.: ' + str(t) + ', Leader Fit: ' + str(leader_fitness)
            print(log_txt)

        # increase iterations
        t = t + 1

    # return leader result
    result.leader_fitness = leader_fitness
    result.leader_solution = solutions[0]
    return  result