# the problem was to count how many rectangles fit into a K - times subdivided square
# after K subdivisions there are n = 2^K cells per side and n+1 grid lines
# equation below derived from "variations without repetition" (n!/(n-k)!) for k - how many gridlines we choose(2) and n - how many gridlines there are on one plane
# it's unoptimized for big K's so wait a while for the output! it can be optimized, but I don't understand how :(
def calc_rects(K: int):
    return pow(pow(2, 2 * K - 1) + pow(2, K - 1), 2) % 1000000009

with open('./input.txt') as f:
    test_cases = f.readline()
    lines = f.readlines()
    lines = [int(x.strip()) for x in lines]
    
    for i, line in enumerate(lines):
        print(f'Case #{i+1}: {calc_rects(line)}')