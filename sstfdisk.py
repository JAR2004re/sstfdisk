def sstf_disk_scheduling(requests, initial_position):
    total_head_movement = 0
    current_position = initial_position

    # Continue until all requests are served
    while requests:
        # Find the nearest request to the current position
        nearest_request = min(requests, key=lambda x: abs(x - current_position))
        
        # Calculate the absolute distance to move
        head_movement = abs(nearest_request - current_position)
        
        # Update total head movement
        total_head_movement += head_movement
        
        # Move the head to the nearest request
        current_position = nearest_request
        
        # Remove the served request from the list
        requests.remove(nearest_request)

    return total_head_movement

# Example usage
if __name__ == "__main__":
    # List of disk requests
    disk_requests = [98, 183, 37, 122, 14, 124, 65, 67]
    
    # Initial head position
    initial_head_position = 53
    
    # Calculate total head movement using SSTF algorithm
    total_movement = sstf_disk_scheduling(disk_requests, initial_head_position)
    
    # Print the total head movement
    print("Total head movement using SSTF algorithm:", total_movement)
