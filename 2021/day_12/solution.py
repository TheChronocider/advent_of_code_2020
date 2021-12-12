from collections import defaultdict

def solution ():
    with open("input.txt") as f:
        data = f.readlines()

        # Default dict is like dict without the missing key issue
        paths = defaultdict(list)

        for line in data:
            a, b = line.strip().split('-')

            paths[a] += [b]
            paths[b] += [a]

        print(pathway_part1(paths=paths))
        print(pathway_part2(paths=paths))


def pathway_part1(paths, seen = set(), cave='start'):
    if cave =='end':
        return 1
    if cave in seen:
        if cave == 'start':
            return 0
        if cave.islower():
            return 0

    pathways = 0
    
    for path in paths[cave]:
        pathways += pathway_part1(paths, seen | {cave}, path)
    
    return pathways

def pathway_part2(paths, visited = 0, seen = set(), cave='start'):
    if cave =='end':
        return 1
    if cave in seen:
        if cave == 'start':
            return 0
        if cave.islower():
            if visited == 1:
                return 0
            else:
                visited = 1

    pathways = 0
    
    for path in paths[cave]:
        pathways += pathway_part2(paths, visited, seen | {cave}, path)
    
    return pathways

solution()
