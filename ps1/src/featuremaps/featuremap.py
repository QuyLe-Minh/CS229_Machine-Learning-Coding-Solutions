import util
import numpy as np
import matplotlib.pyplot as plt

np.seterr(all='raise')


factor = 2.0

class LinearModel(object):
    """Base class for linear models."""

    def __init__(self, theta=None):
        """
        Args:
            theta: Weights vector for the model.
        """
        self.theta = theta

    def fit(self, X, y):
        """Run solver to fit linear model. You have to update the value of
        self.theta using the normal equations.

        Args:
            X: Training example inputs. Shape (n_examples, dim).
            y: Training example labels. Shape (n_examples,).
        """
        # *** START CODE HERE ***
        self.theta = np.linalg.solve(X.T @ X, X.T @ y)
        # *** END CODE HERE ***

    def create_poly(self, k, X):
        """
        Generates a polynomial feature map using the data x.
        The polynomial map should have powers from 0 to k
        Output should be a numpy array whose shape is (n_examples, k+1)

        Args:
            X: Training example inputs. Shape (n_examples, 2).
        """
        # *** START CODE HERE ***
        phi = np.empty([X.shape[0], k+1])
        for i in range(k+1):
            phi[:, i] = X[:,1]**i
        return phi
        # *** END CODE HERE ***

    def create_sin(self, k, X):
        """
        Generates a sin with polynomial featuremap to the data x.
        Output should be a numpy array whose shape is (n_examples, k+2)

        Args:
            X: Training example inputs. Shape (n_examples, 2).
        """
        # *** START CODE HERE ***
        phi = np.empty([X.shape[0], k+2])
        phi[:, :k+1] = self.create_poly(k, X)
        phi[:, k+1] = np.sin(X[:, 1])
        return phi
        # *** END CODE HERE ***

    def predict(self, X):
        """
        Make a prediction given new inputs x.
        Returns the numpy array of the predictions.

        Args:
            X: Inputs of shape (n_examples, dim).

        Returns:
            Outputs of shape (n_examples,).
        """
        # *** START CODE HERE ***
        return self.theta @ X.T
        # *** END CODE HERE ***


def run_exp(train_path, sine=False, ks=[1, 2, 3, 5, 10, 20], filename='plot.png'):
    train_x,train_y=util.load_dataset(train_path,add_intercept=True)
    plot_x = np.ones([1000, 2])
    plot_x[:, 1] = np.linspace(-factor*np.pi, factor*np.pi, 1000)
    plt.figure()
    plt.scatter(train_x[:, 1], train_y)

    for k in ks:
        '''
        Our objective is to train models and perform predictions on plot_x data
        '''
        # *** START CODE HERE ***
        clf = LinearModel()
        if sine:
            phi = clf.create_sin(k, train_x)
            plot_x_adjusted = clf.create_sin(k, plot_x)
        else:
            phi = clf.create_poly(k, train_x)
            plot_x_adjusted = clf.create_poly(k, plot_x)
        clf.fit(phi, train_y)
        plot_y = clf.predict(plot_x_adjusted)
        # *** END CODE HERE ***
        '''
        Here plot_y are the predictions of the linear model on the plot_x data
        '''
        plt.ylim(-2, 2)
        plt.plot(plot_x[:, 1], plot_y, label='k=%d' % k)

    plt.legend()
    plt.savefig(filename)
    plt.clf()


def main(train_path, small_path, eval_path):
    '''
    Run all expetriments
    '''
    # *** START CODE HERE ***
    #run_exp(train_path)
    #run_exp(train_path, True, [0, 1, 2, 3, 5, 10, 20], "sin.png")
    run_exp(small_path, False, [ 1, 2, 5, 10, 20], "small.png")
    # *** END CODE HERE ***

if __name__ == '__main__':
    main(train_path='D:\Coding\ps1\src\\featuremaps\\train.csv',
        small_path='D:\Coding\ps1\src\\featuremaps\small.csv',
        eval_path='D:\Coding\ps1\src\\featuremaps\\test.csv')
