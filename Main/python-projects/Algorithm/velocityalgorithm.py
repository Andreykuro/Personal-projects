def velocity_verlet(x, v, a, dt, num_steps):
    x_history = [x]
    v_history = [v]
    t = 0
    for i in range(num_steps):
        a_new = get_acceleration(x + v * dt + 0.5 * a * dt * dt)
        x += v * dt + 0.5 * a * dt * dt
        v += 0.5 * (a + a_new) * dt
        a = a_new
        t += dt
        x_history.append(x)
        v_history.append(v)
    return x_history, v_history, t
