from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model

# Predict with the model
img_path = "https://cdn.discordapp.com/attachments/1093507477997355078/1093866236141645944/image.png"
results = model(img_path, save=True)  # predict on an image