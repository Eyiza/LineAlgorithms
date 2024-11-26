import matplotlib.pyplot as plt
import pandas as pd

def draw_dda(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Calculate the differences
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the gradient
    if dx == 0:
        gradient = float('inf') # Infinite slope for vertical lines
    else:
        gradient = dy / dx

    # Determine the number of steps required
    steps = max(abs(dx), abs(dy))
    
    # Calculate increment in x and y
    x_increment = dx / steps
    y_increment = dy / steps
    
    # Initialize starting point
    x, y = x1, y1
    points = [(round(x), round(y))]
    
    for _ in range(steps):
        # Increment the x and y values
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))
    
    return points, gradient


# Example usage
point1 = (2, 2)
point2 = (6, 10)

# Get the line points using DDA
dda_points, gradient = draw_dda(point1, point2)

# Dataframe to diplays the points
data = {
    "Step": list(range(len(dda_points))),
    "DDA (x, y)": dda_points
}
df = pd.DataFrame(data)

# Display the points
print(df)

# Unzip the points to plot the line
x_points, y_points = zip(*dda_points)

# Plot the line
plt.plot(x_points, y_points, marker="+", color="blue", label="DDA Points")
plt.title(f"DDA Line Drawing with gradient {gradient:.2f}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
