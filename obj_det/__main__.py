from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model

# Predict with the model
img_path = "https://cdn.discordapp.com/attachments/1093507477997355078/1093546761852813363/fotu_out.png"
results = model(img_path, save=True)  # predict on an image