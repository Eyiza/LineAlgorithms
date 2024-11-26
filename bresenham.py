import matplotlib.pyplot as plt

def draw_bresenham(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1
    x_points, y_points = [x], [y]

    if dx == 0:
        m = 0
    else:
        m = dy / dx

    if m >= 0 and m <= 1:
        d = 2 * dy - dx
        deltaE = 2 * dy
        deltaNE = 2 * (dy - dx)

        while x < x2:
            if d <= 0:
                d += deltaE
                x += 1
            else:
                d += deltaNE
                x += 1
                y += 1

            x_points.append(x)
            y_points.append(y)
    elif m > 1:
        d = dy - 2 * dx
        deltaN = -2 * dx
        deltaNE = 2 * (dy - dx)

        while y < y2:
            if d > 0:
                d += deltaN
                y += 1
            else:
                d += deltaNE
                x += 1
                y += 1

            x_points.append(x)
            y_points.append(y)
    elif m < -1:
        d = dy + 2 * dx
        deltaS = 2 * dx
        deltaSE = 2 * (dy + dx)

        while y > y2:
            if d <= 0:
                d += deltaS
                y -= 1
            else:
                d += deltaSE
                x += 1
                y -= 1

            x_points.append(x)
            y_points.append(y)
    elif m >= -1 and m < 0:
        d = 2 * dy + dx
        deltaE = 2 * dy
        deltaSE = 2 * (dy + dx)

        while x < x2:
            if d > 0:
                d += deltaE
                x += 1
            else:
                d += deltaSE
                x += 1
                y -= 1

            x_points.append(x)
            y_points.append(y)

    return x_points, y_points, m

# Example usage
point1 = (1, 1)
point2 = (8, 5)
x_points, y_points, gradient = draw_bresenham(point1, point2)

plt.figure(figsize=(6, 6))
plt.plot(x_points, y_points, marker="o", color="red")
plt.title(f"Bresenham Line Drawing with gradient {gradient:.2f}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()