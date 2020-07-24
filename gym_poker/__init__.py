"""Register Gym envirnoments for poker poker"""
from gym.envs.registration import register

register(
    id='texas_poker-v0',
    entry_point='gym_poker.envs:PokerEnvV0',
)
