import matplotlib.pyplot as plt

def draw_dda(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Calculate the differences
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the gradient
    if dx == 0:
        gradient = 1.0
    else:
        gradient = dy / dx

    # Determine the number of steps required
    steps = max(abs(dx), abs(dy))
    
    # Calculate increment in x and y
    x_increment = dx / steps
    y_increment = dy / steps
    
    # Initialize starting point
    x, y = x1, y1
    x_points, y_points = [x], [y]
    
    for _ in range(steps):
        # Increment the x and y values
        x += x_increment
        y += y_increment
        x_points.append(round(x))
        y_points.append(round(y))
    
    return x_points, y_points, gradient


# Example usage
point1 = (1, 2)
point2 = (8, 6)

# Get the line points using DDA
x_points, y_points, gradient = draw_dda(point1, point2)

# Plot the line
plt.plot(x_points, y_points, marker="+", color="blue")
plt.title(f"DDA Line Drawing with gradient {gradient:.2f}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
