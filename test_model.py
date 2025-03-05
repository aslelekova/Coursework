from ultralytics import YOLO

model = YOLO("/Users/anastasialelekova/PycharmProjects/sber/yolo_checkpoints/train_100/weights/best.pt")

test_data = "/Users/anastasialelekova/Downloads/data/train/dirty"  # Путь к папке с тестовыми изображениями
results = model.predict(test_data, imgsz=640, device="cpu")

# Показать результаты
for result in results:
    result.show()
    result.save()

# Сохранить результаты
results.save()

# Вывести метрики
print("Precision:", results.pf1)
print("Recall:", results.recall)
print("mAP:", results.maps)