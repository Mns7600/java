n = int(input("Number of instructions: "))
k = int(input("Number of pipeline stages: "))
t = float(input("Clock time per stage (ns): "))
non_cycles = n * k
pipe_cycles = n + k - 1
non_time = non_cycles * t
pipe_time = pipe_cycles * t
speedup = non_time / pipe_time
efficiency = (speedup / k) * 100
throughput = n / pipe_time
print(f"\nNon-pipelined clocks: {non_cycles}")
print(f"Pipelined clocks: {pipe_cycles}")
print(f"Execution time (Non-pipeline): {non_time:.2f} ns")
print(f"Execution time (Pipeline): {pipe_time:.2f} ns")
print(f"Speedup: {speedup:.2f}")
print(f"Efficiency: {efficiency:.2f}%")
print(f"Throughput: {throughput:.6f} instructions/ns")