import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 상수
G = 6.674 * 10**-11  # 중력 상수

# 물체 클래스
class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

    def apply_gravity(self, other, dt):
        # 두 물체 사이의 거리 벡터
        diff = other.position - self.position
        distance = np.linalg.norm(diff)
        if distance == 0:
            return  # 동일한 위치에 있으면 중력을 계산하지 않음

        # 중력 가속도 계산
        force_magnitude = G * self.mass * other.mass / distance**2
        force_direction = diff / distance
        force = force_direction * force_magnitude

        # 가속도 계산 및 속도 업데이트
        acceleration = force / self.mass
        self.velocity += acceleration * dt

    def move(self, dt):
        # 위치 업데이트
        self.position += self.velocity * dt

# 초기 값들
mass1 = 5.974 * 10**24  # 지구 질량 (kg)
mass2 = 7.348 * 10**22  # 달 질량 (kg)
distance_initial = 384400000  # 초기 거리 (지구와 달 거리, m)

body1 = Body(mass1, [0, 0], [0, 0])
body2 = Body(mass2, [distance_initial, 0], [0, 1022])  # m/s (달 궤도 속도 근사치)

# 시뮬레이션 파라미터
time_step = 3600  # 1 시간
num_steps = 24 * 30  # 30 days

# 초기화 함수
def init():
    ln1.set_data([], [])
    ln2.set_data([], [])
    return ln1, ln2

# 업데이트 함수
def update(frame):
    body1.apply_gravity(body2, time_step)
    body2.apply_gravity(body1, time_step)

    body1.move(time_step)
    body2.move(time_step)

    # 여기서 한 개의 점만을 나타내기 위해 리스트 또는 배열로 전달하도록 수정
    ln1.set_data([body1.position[0]], [body1.position[1]])
    ln2.set_data([body2.position[0]], [body2.position[1]])

    return ln1, ln2

# Figure 설정
fig, ax = plt.subplots()
ax.set_xlim(-5e8, 5e8)
ax.set_ylim(-5e8, 5e8)
ln1, = ax.plot([], [], 'bo', label='Body 1 (Earth)')
ln2, = ax.plot([], [], 'ro', label='Body 2 (Moon)')

# 애니메이션 생성
ani = FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=True, interval=30, repeat=False)
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.legend()
plt.title('Gravity Simulation')
plt.show()