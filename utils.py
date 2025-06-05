

def flood_fill_exterior(width_tiles, height_tiles, blocked_tiles):
    visited = set()
    stack = []

    # start flood from all border tiles
    for x in range(width_tiles):
        stack.append((x, 0))
        stack.append((x, height_tiles - 1))
    for y in range(height_tiles):
        stack.append((0, y))
        stack.append((width_tiles - 1, y))
    
    while stack:
        x, y = stack.pop()
        if (x, y) in visited or (x, y) in blocked_tiles:
            continue
        
        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width_tiles and 0 <= ny < height_tiles:
                stack.append((nx, ny))
        
    return visited