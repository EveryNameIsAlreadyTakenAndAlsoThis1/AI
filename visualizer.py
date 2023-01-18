import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
    def __init__(self, file_name):
        with open(file_name) as file:
            self.games = []
            self.actions = []
            self.rewards = []
            self.scores = []
            self.times = []
            self.epsilons = []
            self.learning_rates = []

            line = file.readline()

            while line:
                self.games.append(line)
                file.readline()
                self.actions.append([float(item) for item in file.readline().split(',')])
                file.readline()
                self.rewards.append([float(item) for item in file.readline().split(',')])
                self.scores.append(sum(self.rewards[-1]))
                file.readline()
                self.times.append(float(file.readline()))
                file.readline()
                self.epsilons.append(float(file.readline()))
                file.readline()
                self.learning_rates.append(float(file.readline()))

                line = file.readline()

    def visualize_data(self, average=False, moving_average_threshold=100):
        fig, score_plot = plt.subplots()
        epsilon_plot = score_plot.twinx()

        x_axis = np.arange(0, len(self.games))

        lines = [
            score_plot.plot(x_axis, self.scores, 'g-', label='Score')[0],
            epsilon_plot.plot(x_axis, self.epsilons, 'b-', label='Epsilon')[0]
        ]

        if average:
            lines.append(score_plot.plot(x_axis, self.__moving_average(self.scores, moving_average_threshold), 'r-', label='Moving average score')[0])

        score_plot.set_xlabel('Game')
        score_plot.set_ylabel('Score', color='g')
        epsilon_plot.set_ylabel('Epsilon', color='b')

        fig.tight_layout(pad=3, w_pad=0.5, h_pad=1.0)
        score_plot.legend(lines, [line.get_label() for line in lines], loc='upper center', bbox_to_anchor=(0.5, -0.125), fancybox=True, shadow=True, ncol=5)

        plt.show()

    @staticmethod
    def __moving_average(values, threshold):
        average_values = []
        t = 0

        for i in range(len(values)):
            if i < threshold - 1:
                average_values.append(np.average(values[:i+1]))
            else:
                average_values.append(np.average(values[t:i+1]))
                t += 1

        return average_values