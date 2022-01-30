import numpy
import scipy.special

class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        # 返回符合正态分布的随机值，分别是均值、标准差和维度（隐藏层*输入层）
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hondes))
        self.lr = learningrate  # 学习速度
        self.activation_function = lambda x:scipy.special.expit(x)
        # S函数嗷

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin = 2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(hidden_outputs, self.who)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(hidden_outputs, self.who)
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)
        self.who += self.lr * numpy.dot((output_errors * final_inputs * (1.0 - final_inputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        pass

def main():
    return 0

if __name__ == '__main__' :
    main()