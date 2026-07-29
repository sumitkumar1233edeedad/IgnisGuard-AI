from django.shortcuts import render
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import base64
from PIL import Image
import io
import glob
import shutil
import tempfile
from django.http import JsonResponse
from .model_loading import get_model


model = get_model()

# Create your views here.
def home(request):
    return render(request, 'home.html')


def image_detection(request):

    context = {}

    if request.method == "POST" and request.FILES.get("image"):

        uploaded_file = request.FILES["image"]

        # Read image directly from uploaded data
        image = Image.open(uploaded_file).convert("RGB")

        # Convert PIL image for YOLO
        results = model(image)

        # Prediction image with boxes
        predicted = results[0].plot()

        # Convert prediction to PIL
        predicted_img = Image.fromarray(predicted)

        # Original image to base64
        original_buffer = io.BytesIO()
        image.save(original_buffer, format="JPEG")

        original_base64 = base64.b64encode(
            original_buffer.getvalue()
        ).decode()


        # Prediction image to base64
        prediction_buffer = io.BytesIO()
        predicted_img.save(
            prediction_buffer,
            format="JPEG"
        )

        prediction_base64 = base64.b64encode(
            prediction_buffer.getvalue()
        ).decode()


        context = {
            "original_image": original_base64,
            "prediction_image": prediction_base64,
        }


    return render(
        request,
        "image.html",
        context
    )


def live_detection(request):
    return render(request, "live.html")


def predict_frame(request):

    if request.method == "POST":

        image_file = request.FILES["frame"]

        image = Image.open(image_file).convert("RGB")


        # YOLO prediction
        results = model(image)


        # Draw boxes
        predicted = results[0].plot()


        predicted_image = Image.fromarray(predicted)


        # Convert to base64
        buffer = io.BytesIO()

        predicted_image.save(
            buffer,
            format="JPEG"
        )


        img_base64 = base64.b64encode(
            buffer.getvalue()
        ).decode()


        return JsonResponse({
            "image": img_base64
        })


# def video_detection(request):
#     context = {}

#     if request.method == "POST" and request.FILES.get("video"):

#         uploaded_video = request.FILES["video"]

#         # Create temporary file
#         with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp:
#             for chunk in uploaded_video.chunks():
#                 temp.write(chunk)
#             temp_path = temp.name

#         # Run YOLO
#         model.predict(
#             source=temp_path,
#             save=True,
#             conf=0.25
#         )

#         # Find latest prediction folder
#         latest_folder = max(
#             glob.glob("runs/detect/predict*"),
#             key=os.path.getmtime
#         )

#         predicted_video = os.path.join(
#             latest_folder,
#             os.path.basename(temp_path)
#         )

#         # Copy result to MEDIA/output
#         output_dir = os.path.join(settings.MEDIA_ROOT, "output")
#         os.makedirs(output_dir, exist_ok=True)

#         output_name = os.path.basename(predicted_video)
#         destination = os.path.join(output_dir, output_name)

#         shutil.copy(predicted_video, destination)

#         # Delete temporary uploaded file
#         if os.path.exists(temp_path):
#             os.remove(temp_path)

#         context["video_url"] = settings.MEDIA_URL + "output/" + output_name
#         context["video_name"] = output_name

#     return render(request, "video.html", context)


# def delete_video(request):
#     if request.method == "POST":

#         filename = request.POST.get("filename")

#         file_path = os.path.join(
#             settings.MEDIA_ROOT,
#             "output",
#             filename
#         )

#         if os.path.exists(file_path):
#             os.remove(file_path)

#         return JsonResponse({"status": "success"})

#     return JsonResponse({"status": "error"})