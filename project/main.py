from manim import *

from intro_scenes import Greetings, Memory, MemoryProblem
from tree_scenes import GamePrediction, MinimaxValue, EvaluationFunction

config.media_width = "75%"
config.verbosity = "WARNING"


class MainScene(Scene):
    def construct(self):
        Greetings.construct(self)
        self.clear()
        Memory.construct(self)
        self.clear()
        MemoryProblem.construct(self)
        self.clear()
        GamePrediction.construct(self)
        self.clear()
        MinimaxValue.construct(self)
        self.clear()
        EvaluationFunction.construct(self)
        self.clear()
        EvaluationFunction.construct(self)
        self.clear()
