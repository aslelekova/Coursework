from ultralytics import YOLO

model = YOLO("runs/detect/train13/weights/best.onnx")

test_data = "/path/to/test/data"  # Путь к папке с тестовыми изображениями
results = model.predict(test_data, imgsz=640, device="cpu")

# Показать результаты
results.show()

# Сохранить результаты
results.save()

# Вывести метрики
print("Precision:", results.pf1)
print("Recall:", results.recall)
print("mAP:", results.maps)