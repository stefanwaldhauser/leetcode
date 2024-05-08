# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1406
# solve a problem where you need to maximize the number of burgers ordered within a given time t, with each burger preparation taking either m or n minutes.
# If it's not possible to exactly use up all t minutes, the solution aims to minimize the unused time, which is then considered as "beer time".


# We first solve another problem:
# Return the maximum number of burgers (either n or m burgers) to make up exactly or -1 if it can not be solved exactly using n or m burges
def solve_exact(m,n,t):
    if t < 0: # Invalid Choice
        return -1
    if t == 0: #  # If exactly 0 time is left, it means we've used up the time perfectly without needing a burger
        return 0 # No time means no burger
    # choose m (-> assume the function works for smaller problem t-m) "Assuming we spend m minutes on this burger, what's the maximum number of burgers we can get in the remaining time?"
    m_choice_result = solve_exact(m,n, t-m) # Easier problem where one m burger has been solved already
    # choose n (-> assume function works for smaller problem t-n) "Assuming we spend n minutes on this burger, what's the maximum number of burgers we can get in the remaining time?"
    n_choice_result = solve_exact(m,n, t-n) # Easier problem where one n burger has been solved already
    # m_choice or n_choice is either -1, 0, or a positive integer. We want the maximum of it
    best_outcome = max(m_choice_result, n_choice_result)
    if best_outcome == -1: # smaller problem already not solvable with m or n so larger definitely also not solvable
        return -1
    return best_outcome + 1 # one burger more


# Now that we can solve the above problem, we can solve the real problem.
# If we can not solve it exactly, try to solve the -1 version exactly and then return the remainder as beer time

def solve(m,n,t):
    max_burgers = -1
    beer_time = 0
    while beer_time <= t:
        max_burgers = solve_exact(m, n, t-beer_time)
        if max_burgers != -1:
            break;
        beer_time = beer_time +1
    if beer_time == 0:
        print(str(max_burgers))
    else:
        print(str(max_burgers) + " " + str(beer_time))


try:
    while True:
        line = input()
        if not line:  # Check if the line is empty; this might happen depending on your EOF handling
            break
        parts = line.split()
        _m, _n, _t = map(int, parts)
        solve(_m, _n, _t)
except EOFError:
    pass  # End of input
