

def solve(value):
    return {v: [k for k, item in value.items() if item == v] for v in sorted(set(value.values()))}
