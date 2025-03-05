from ultralytics import YOLO
import cv2
import os
import shutil

# Загрузка модели для детекции банкоматов
detection_model = YOLO("/Users/anastasialelekova/PycharmProjects/pythonProject9/yolo_checkpoints/train_100/weights/best.pt")  # Подставьте путь к вашей модели детекции

# Пути к датасету с изображениями
input_dataset_path = "/Users/anastasialelekova/PycharmProjects/pythonProject9/c-1"
output_dataset_path = "processed_dataset"


def detect_atm_and_crop(image_path, save_path):
    """ Детекция банкоматов и обрезка найденных объектов """
    img = cv2.imread(image_path)
    results = detection_model(img)

    # Инициализация переменной save_filename для возврата в случае отсутствия детекции
    save_filename = None

    for i, box in enumerate(results[0].boxes.xyxy):  # Получаем координаты боксов
        x1, y1, x2, y2 = map(int, box[:4])
        cropped_img = img[y1:y2, x1:x2]
        save_filename = f"{save_path}/{os.path.basename(image_path).split('.')[0]}_{i}.jpg"
        cv2.imwrite(save_filename, cropped_img)

    # Возвращаем сохранённый файл, если были детекции
    return save_filename

# Очистка папки processed_dataset
if os.path.exists(output_dataset_path):
    shutil.rmtree(output_dataset_path)
os.makedirs(f"{output_dataset_path}/train/clean", exist_ok=True)
os.makedirs(f"{output_dataset_path}/train/dirty", exist_ok=True)
os.makedirs(f"{output_dataset_path}/val/clean", exist_ok=True)
os.makedirs(f"{output_dataset_path}/val/dirty", exist_ok=True)

# Обрабатываем датасет: детекция банкоматов и сохранение кропнутых изображений
for phase in ["train", "val"]:
    for category in ["clean", "dirty"]:
        input_folder = os.path.join(input_dataset_path, phase, category)
        output_folder = os.path.join(output_dataset_path, phase, category)

        for img_file in os.listdir(input_folder):
            img_path = os.path.join(input_folder, img_file)
            detect_atm_and_crop(img_path, output_folder)
