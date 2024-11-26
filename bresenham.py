import matplotlib.pyplot as plt
import pandas as pd

def draw_bresenham(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Calculate the differences
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Calculate the step directions
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    # Initialize starting point
    x, y = x1, y1
    points = [(x, y)]
    p_values = []

    # Calculate the gradient
    if dx == 0:
        gradient = float('inf')
    else:
        gradient = dy / dx

    # Initialize the decision parameter
    if dx > dy: # Shallow Slopes i.e |m| < 1
        p = (2 * dy) - dx
        p_values.append(p)
        while x != x2:
            x += step_x
            if p > 0:
                y += step_y
                p -= (2 * dx)
            p += (2 * dy)
            points.append((x, y))
            p_values.append(p)
    else: # Steep Slopes i.e |m| > 1
        p = (2 * dx) - dy
        p_values.append(p)
        while y != y2:
            y += step_y
            if p > 0:
                x += step_x
                p -= (2 * dy)
            p += (2 * dx)
            points.append((x, y))
            p_values.append(p)

    return points, p_values, gradient

# Example usage
point1 = (2, 2)
point2 = (6, 10)

# Get the line points using Bresenham
bresenham_points, p_values, gradient = draw_bresenham(point1, point2)

# Dataframe to diplays the points
data = {
    "Step": list(range(len(bresenham_points))),
    "Bresenham (x, y)": bresenham_points,
    "Decision Parameter (p)": p_values,
}
df = pd.DataFrame(data)

# Display the points
print(df)

# Unzip the points to plot the line
x_points, y_points = zip(*bresenham_points)

# Plot the line
plt.plot(x_points, y_points, marker="o", color="red")
plt.title(f"Bresenham Line Drawing with gradient {gradient:.2f}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()