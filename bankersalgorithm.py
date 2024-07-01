def calculate_available_resources(total_resources, allocations):
    available = [total - sum(allocation) for total, allocation in zip(total_resources, zip(*allocations))]
    return available
def check_safe_sequence(avail, need, f, alloc):
    n = len(need)
    r = len(avail)
    work = avail[:]
    finish = f[:]
    sequence = []
    while True:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(r)):
                for j in range(r):
                    work[j] += alloc[i][j]
                finish[i] = True
                sequence.append(i)
                found = True
        if not found:
            break
    if all(finish):
        print("The SAFE Sequence is as follows:")
        print("P" + " -> P".join(map(str, sequence)))
    else:
        print("Deadlock Detected")
def banker_algorithm():
    n = int(input("Enter the number of processes: "))
    r = int(input("Enter the number of resources: "))
    alloc = []
    print("Enter the Allocation Matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        alloc.append(row)
    max = []
    print("Enter the MAX Matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        max.append(row)
    total_resources = list(map(int, input("Enter the Total Resources: ").split()))
    avail = calculate_available_resources(total_resources, alloc)
    f = [0] * n
    need = [[0] * r for _ in range(n)]
    for i in range(n):
        for j in range(r):
            need[i][j] = max[i][j] - alloc[i][j]
    print("Need Matrix:")
    for row in need:
        print(row)
    print("Available Resources:")
    print(avail)
    check_safe_sequence(avail, need, f, alloc)
banker_algorithm()
