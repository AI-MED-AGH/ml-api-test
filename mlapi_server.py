import numpy as np
from fastmlapi import MLController, preprocessing, postprocessing


def model(X: np.ndarray) -> np.ndarray:
    return np.mod(X, 2)


class MyClassifier(MLController):
    model_name = "my-classifier"
    model_version = "1.0.0"

    def load_model(self):
        return model

    @preprocessing
    def preprocess(self, data: list[int]) -> np.ndarray:
        return np.array(data, dtype=int)

    @postprocessing
    def postprocess(self, prediction: np.ndarray) -> list[int]:
        response = prediction.tolist()
        return response


if __name__ == "__main__":
    MyClassifier().run()
