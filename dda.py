import matplotlib.pyplot as plt

def draw_dda(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    dx = x2 - x1
    dy = y2 - y1

    gradient = dy / dx
    steps = max(abs(dx), abs(dy))
    
    x_increment = dx / steps
    y_increment = dy / steps
    
    x, y = x1, y1
    x_points, y_points = [x], [y]
    
    for i in range(steps):
        x += x_increment
        y += y_increment
        x_points.append(round(x))
        y_points.append(round(y))
    
    return x_points, y_points, gradient

# Example usage
point1 = (1, 1)
point2 = (8, 5)
x_points, y_points, gradient = draw_dda(point1, point2)

plt.figure(figsize=(6, 6))
plt.plot(x_points, y_points, marker="+", color="blue")
plt.title(f"DDA Line Drawing with gradient {gradient:.2f}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
