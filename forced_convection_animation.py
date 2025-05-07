# forced_convection_animation.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_animation():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 2)
    ax.set_title('Forced Convection: Air Flow Over Heated Surface')
    ax.set_xlabel('Pipe Length')
    ax.set_ylabel('Height')

    pipe, = ax.plot([], [], lw=8, color='orangered', alpha=0.8)

    num_particles = 40
    x = np.linspace(0, 10, num_particles)
    y = np.random.uniform(-1.5, 1.5, size=num_particles)
    colors = np.full(num_particles, 'skyblue')
    particles = ax.scatter(x, y, c=colors, s=30)

    def init():
        pipe.set_data([0, 10], [0, 0])
        return pipe, particles

    def animate(frame):
        new_x = (x + 0.1 * frame) % 10
        new_colors = ['red' if abs(yi) < 0.4 else 'skyblue' for yi in y]
        particles.set_offsets(np.column_stack((new_x, y)))
        particles.set_color(new_colors)
        return pipe, particles

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=False)
    return ani
