def solve(m,n,t):
    dp = {}
    # we solve now the problem from the smallest to the largest to ensure we always have solved the smaller problems before we need them
    dp[0] = 0 # _t = 0
    for _t in range(1, t+1):
        m_result = -1 # -1 means no exact solution
        n_result = -1 # -1 means no exact solution
        if _t >= m:
            m_result = dp[_t-m]
            if m_result != -1:
                m_result = m_result + 1
        if _t >= n:
            n_result = dp[_t-n]
            if n_result != -1:
                n_result = n_result + 1
        dp[_t] = max(m_result, n_result)

    # dp array is now fully built and will contain solution for t also
    max_burgers = -1
    beer_time = 0
    while beer_time <= t:
        max_burgers = dp[t-beer_time]
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
