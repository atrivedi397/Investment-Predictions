from sklearn.externals import joblib
import joblib

"""
The arguments are the model/classifier itself, and the filename by which it is to be saved
As, the new versions of the scikit models may not support its previous versions of pickle file,
hence the name also includes the scikit learn library version with the filename"""


def save_model(model, save_as_filename):
    scikit_learn_version = joblib.__version__
    save_as_filename = save_as_filename + scikit_learn_version + ".pkl"
    joblib.dump(model, save_as_filename)    # this saves the model
    print(f"saved as {save_as_filename}")
