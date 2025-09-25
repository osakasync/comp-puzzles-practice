# after a while of scribbling in paint and trying random stuff I noticed that
# the number of possible rectangles along one row is the sum of 2^K ... 1
# where 2^K is the number of grid cells after K subdivisions, In this file I calculate it via the Gauss equation for the sum of the first n positive integers: (n*(n+1))/2
# weirdly enough when you square that number you get the total rectangles in the grid! (horizontal choices x vertical choices)
# so the final formula became: rectangles = ((n*(n+1))/2)^2 where n = 2^K
# this is exactly the same result as solution.py,
# but discovered through randomness and boredom :P Most importantly it runs fast!

MOD = 1000000009

def calc_rects(K: int):
    start = pow(2, K, MOD)
    _sum = (start * (start + 1)) // 2
    
    return pow(_sum, 2, MOD)

with open('./input.txt') as f:
    test_cases = f.readline()
    lines = f.readlines()
    lines = [int(x.strip()) for x in lines]

    with open('./output.txt', 'w') as output_f:
        for i, line in enumerate(lines):
            output_f.write(f'Case #{i+1}: {calc_rects(line)}\n')


