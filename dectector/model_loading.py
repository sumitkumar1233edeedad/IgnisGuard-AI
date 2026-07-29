import os
from django.conf import settings
from ultralytics import YOLO

_model = None

def get_model():
    global _model

    if _model is None:
        model_path = os.path.join(
            settings.BASE_DIR,
            "models",
            "fired_model.pt"
        )

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found: {model_path}")

        _model = YOLO(model_path)

    return _model