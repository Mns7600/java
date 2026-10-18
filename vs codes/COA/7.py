def simple_memory_hierarchy():
    n = int(input("Enter number of hierarchy levels: "))
    total_cost = 0
    total_size = 0
    avg_time_ns = 0
    miss_ratio = 1  # Probability of reaching the current level (initially 100%)
    
    for i in range(n):
        print(f"\nLevel {i + 1}:")
        c = float(input("Cost per bit (Rs/-): "))
        s = int(input("Size (bits): "))
        h = float(input("Hit ratio (0 to 1): "))
        ta = float(input("Access time (microsec): ")) * 1000  # Convert to nanosec
        
        # Accumulate totals inside the loop
        total_cost += c * s
        total_size += s
        
        # Add access time incurred at this level (miss probability * access time)
        avg_time_ns += miss_ratio * ta
        
        # Update cumulative miss ratio for the next level
        miss_ratio *= 1 - h

    avg_cost = total_cost / total_size if total_size else 0
    avg_time_us = avg_time_ns / 1000
    
    print(f"\nAverage Cost per bit: Rs/- {avg_cost:.4f}")
    print(f"Average Access Time: {avg_time_us:.4f} microsec")

if __name__ == "__main__":
    simple_memory_hierarchy()