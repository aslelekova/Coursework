from ultralytics import YOLO

model = YOLO("runs/detect/train13/weights/best.onnx")

test_data = "/path/to/test/data"
results = model.predict(test_data, imgsz=640, device="cpu")

results.show()

results.save()

print("Precision:", results.pf1)
print("Recall:", results.recall)
print("mAP:", results.maps)
