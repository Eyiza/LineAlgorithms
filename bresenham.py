import matplotlib.pyplot as plt

def draw_bresenham(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Calculate the differences
    dx = x2 - x1
    dy = y2 - y1

    # Initialize starting point
    x, y = x1, y1
    x_points, y_points = [x], [y]

    # Calculate the gradient
    if dx == 0:
        gradient = 0
    else:
        gradient = dy / dx

    # Calculate the step directions
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    # Initialize the decision parameter
    if dx > dy: # Shallow Slopes i.e |m| < 1
        p = (2 * dy) - dx
        while x != x2:
            x += step_x
            if p >= 0:
                y += step_y
                p -= (2 * dx)
            p += (2 * dy)
            x_points.append(x)
            y_points.append(y)
    else: # Steep Slopes i.e |m| > 1
        p = (2 * dx) - dy
        while y != y2:
            y += step_y
            if p >= 0:
                x += step_x
                p -= (2 * dy)
            p += (2 * dx)
            x_points.append(x)
            y_points.append(y)

    return x_points, y_points, gradient

# Example usage
point1 = (1, 1)
point2 = (1, 5)

# Get the line points using Bresenham
x_points, y_points, gradient = draw_bresenham(point1, point2)

# Plot the line
plt.plot(x_points, y_points, marker="o", color="red")
plt.title(f"Bresenham Line Drawing with gradient {gradient:.2f}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()