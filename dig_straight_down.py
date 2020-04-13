import random

import gym
import minerl

print(minerl)

env = gym.make('MineRLTreechop-v0')
obs = env.reset()

while True:
    action = env.action_space.noop()
    action['camera'] = [180, random.randrange(-1, 2)]
    action['attack'] = 1

    obs, reward, done, info = env.step(
        action)
    env.render()
