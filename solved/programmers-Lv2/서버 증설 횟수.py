def solution(players, m, k):
    servers = []

    count = 0
    num_of_servers = 0
    for t in range(len(players)):

        need = players[t] // m
        num_of_scale = need - num_of_servers
        if num_of_scale > 0:
            servers.append([t + k, num_of_scale])
            count += num_of_scale
            num_of_servers += num_of_scale

        while len(servers) > 0 and servers[0][0] == t + 1:
            exit_servers = servers.pop(0)
            num_of_servers -= exit_servers[1]

    return count