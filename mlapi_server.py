import os
import numpy as np
from fastmlapi import MLController, preprocessing, postprocessing
from fastapi.staticfiles import StaticFiles


def model(X: np.ndarray) -> np.ndarray:
    return np.mod(X, 2)


class MyClassifier(MLController):
    model_name = "my-classifier"
    model_version = "1.0.0"

    def _setup_static_frontend(self, app, frontend_dir: str):
        app.mount("/{frontend_dir}", StaticFiles(directory=frontend_dir, html=True), name="static")

    def load_model(self):
        self._setup_static_frontend(self.app, "frontend")
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
