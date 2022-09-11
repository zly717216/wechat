from GroupRobot import Robot as R


__version__ = '1.1.0'
__author__ = 'zly'
__email__ = 'zly717216@163.com'
__publish__ = '2022-09-11'

Robot = R()


def set_token(token: str):
    Robot.set_token(token)


__all__ = [
    'Robot', '__version__', '__author__', '__email__',
    '__publish__', 'set_token'
]
