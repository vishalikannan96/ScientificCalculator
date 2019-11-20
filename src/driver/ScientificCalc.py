import math
import logging

logging.basicConfig(filename="configfile.log", level=logging.ERROR, filemode='w', format='%(asctime)s:%('
                                                                                         'levelname)s:%(message)s')


class ScientificCalc:

    def __init__(self):
        self.angle = 0
        self.tanhx = 0

    @classmethod
    def calculate_sin(self, angle):
        """A method to calculate tanh"""
        try:
            value = float(angle)
            if value:
                return math.sin(float(angle))
            else:
                raise ValueError
        except ValueError as e:
            logging.error(e.message)
            return "ValueError(enter a only number)"
