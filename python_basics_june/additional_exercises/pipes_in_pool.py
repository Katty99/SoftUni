volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

liters_filled = hours * (pipe_1 + pipe_2)
percentage_filled = hours * (pipe_1 + pipe_2) / volume * 100
pipe_1_contribution = pipe_1 * hours / liters_filled * 100
pipe_2_contribution = pipe_2 * hours / liters_filled * 100

if liters_filled <= volume:
    print(f'The pool is {percentage_filled:.2f}% full. Pipe 1: {pipe_1_contribution:.2f}%. Pipe 2: {pipe_2_contribution:.2f}%.')
else:
    difference = liters_filled - volume
    print(f'For {hours:.2f} hours the pool overflows with {difference:.2f} liters')