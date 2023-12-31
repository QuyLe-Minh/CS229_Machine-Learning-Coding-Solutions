import numpy as np
import util


def main(train_path, valid_path, save_path, plot_path):
    """Problem: Gaussian discriminant analysis (GDA)

    Args:
        train_path: Path to CSV file containing dataset for training.
        valid_path: Path to CSV file containing dataset for validation.
        save_path: Path to save predicted probabilities using np.savetxt().
    """
    # Load dataset
    x_train, y_train = util.load_dataset(train_path, add_intercept=False)
    x_val, y_val = util.load_dataset(valid_path, add_intercept=False)
    gda = GDA()
    gda.fit(x_train,y_train)
    y_pred = gda.predict(x_val)
    util.plot(x_val, y_val, gda.theta, plot_path)
    np.savetxt(save_path, y_pred)

    # *** START CODE HERE ***
    # Train a GDA classifier
    # Plot decision boundary on validation set
    # Use np.savetxt to save outputs from validation set to save_path
    # *** END CODE HERE ***


class GDA:
    """Gaussian Discriminant Analysis.

    Example usage:
        > clf = GDA()
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """
    def __init__(self, step_size=0.01, max_iter=10000, eps=1e-5,
                 theta_0=None, verbose=True):
        """
        Args:
            step_size: Step size for iterative solvers only.
            max_iter: Maximum number of iterations for the solver.
            eps: Threshold for determining convergence.
            theta_0: Initial guess for theta. If None, use the zero vector.
            verbose: Print loss values during training.
        """
        self.theta = theta_0
        self.step_size = step_size
        self.max_iter = max_iter
        self.eps = eps
        self.verbose = verbose

    def fit(self, x, y):
        """Fit a GDA model to training set given by x and y by updating
        self.theta.

        Args:
            x: Training example inputs. Shape (n_examples, dim).
            y: Training example labels. Shape (n_examples,).
        """
        # *** START CODE HERE ***
        # Find phi, mu_0, mu_1, and sigma
        # Write theta in terms of the parameters
        m = y.shape[0]
        phi = np.mean(y)
        mu_0 = np.sum(x[y==0], axis = 0)/(phi*m)
        mu_1 = np.sum(x[y==1], axis = 0)/((1-phi)*m)
        mu = np.where(y.reshape(-1, 1), mu_1, mu_0)
        sigma = ((x-mu).T @ (x-mu))/m
        self.theta = np.zeros((x.shape[1]+1))
        self.theta[1:] = (mu_1 - mu_0).T @ np.linalg.inv(sigma)
        self.theta[0] = -np.log((1-phi)/phi) + ((mu_0 - mu_1).T @ np.linalg.inv(sigma) @ (mu_0+mu_1))/2
        # *** END CODE HERE ***
        

    def predict(self, x):
        """Make a prediction given new inputs x.

        Args:
            x: Inputs of shape (n_examples, dim).

        Returns:
            Outputs of shape (n_examples,).
        """
        # *** START CODE HERE ***
        # *** END CODE HERE
        z = (self.theta[1:] @ x.T) + self.theta[0]
        return 1/(1+np.exp(-z))

if __name__ == '__main__':
    main(train_path='D:\Coding\ps1\src\linearclass\ds1_train.csv',
         valid_path='D:\Coding\ps1\src\linearclass\ds1_valid.csv',
         save_path='gda_pred_1.txt',
         plot_path='gda_1.jpg')

    main(train_path='D:\Coding\ps1\src\linearclass\ds2_train.csv',
         valid_path='D:\Coding\ps1\src\linearclass\ds2_valid.csv',
         save_path='gda_pred_2.txt',
         plot_path='gda_2.jpg')
