# -*- coding: utf-8 -*-
#####
#Backpropagation Network
#
#Created on Sat Dec 24 11:58:14 2016
#
#By Shu Cheng
####

import pycuda.autoinit
import numpy as np
import matplotlib.pyplot as plt


def sigmod(z):
    return 1.0 / (1.0 + np.exp(-z))


class nn(object):
    def __init__(self, lr=0.1, lda=0.0, te=1e-5, epoch=100, size=None):
        self.learningRate = lr
        self.lambda_ = lda
        self.thresholdError = te
        self.maxEpoch = epoch
        self.size = size
        self.W = []
        self.b = []
        self.init()

    def init(self):
        for i in range(len(self.size)-1):
            self.W.append(np.mat(np.random.uniform(-0.5, 0.5, size=(self.size[i+1], self.size[i]))))
            self.b.append(np.mat(np.random.uniform(-0.5, 0.5, size=(self.size[i+1], 1))))

    def forwardPropagation(self, item=None):
        a = [item]
        for wIndex in range(len(self.W)):
            a.append(sigmod(self.W[wIndex]*a[-1]+self.b[wIndex]))
        return a

    def backPropagation(self, label=None, a=None):
        # print "backPropagation--------------------begin"
        delta = [(a[-1]-label)*a[-1]*(1.0-a[-1])]
        for i in range(len(self.W)-1):
            abc = np.multiply(a[-2-i], 1-a[-2-i])
            cba = np.multiply(self.W[-1-i].T*delta[-1], abc)
            delta.append(cba)
        for j in range(len(delta)):
            ads = delta[j]*a[-2-j].T
            # print self.W[-1-j].shape, ads.shape, self.b[-1-j].shape, delta[j].shape
            self.W[-1-j] = self.W[-1-j]-self.learningRate*(ads+self.lambda_*self.W[-1-j])
            self.b[-1-j] = self.b[-1-j]-self.learningRate*delta[j]
        # print "backPropagation--------------------finish"
        error = 0.5*(a[-1]-label)**2
        return error

    def train(self, input_=None, target=None, show=10):
        error_rate = []
        for ep in range(self.maxEpoch):
            error = []
            for itemIndex in range(input_.shape[1]):
                a = self.forwardPropagation(input_[:, itemIndex])
                e = self.backPropagation(target[:, itemIndex], a)
                error.append(e[0, 0])
            tt = sum(error)/len(error)
            if tt < self.thresholdError:
                print("Finish {0}: ".format(ep), tt)
                return
            elif ep % show == 0:
                print("epoch {0}".format(ep), 'error rate: ', tt)
                error_rate.append(tt)
        print(error_rate)
        plt.plot(error_rate)

    def sim(self, inp=None):
        return self.forwardPropagation(item=inp)[-1]


if __name__ == "__main__":
    lr = 0.2    # learning rate
    lda = 0.0    # lambda
    te = 1e-5    # threshold error
    epoch = 100    # times of epochs
    size = [1, 6, 6, 6, 1]    # neural network size
    tt = np.arange(0, 6.28, 0.01)
    labels = np.zeros_like(tt)
    tt = np.mat(tt)
    labels = np.sin(tt)*0.5+0.5
    labels = np.mat(labels)
    model = nn(lr, lda, te, epoch, size)
    model.train(input_=tt, target=labels, show=1)  
    sims = [model.sim(tt[:, idx])[0, 0] for idx in range(tt.shape[1])]  
    xx = tt.tolist()[0]  
    plt.figure()  
    plt.plot(xx, labels.tolist()[0], xx, sims, 'r')  
    plt.show() 

