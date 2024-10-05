from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, Dropout, Conv2D, MaxPooling2D, Flatten
from PIL import Image
import cv2
import numpy as np
from ultralyticsplus import YOLO, render_result
from uuid import uuid4


class crop_health_detection:
    
    def __init__(self, img_address):
        
        self.image_addr = img_address
        self.classes = {'Healthy': 0, 'Unhealthy': 1}
        self.leaf_classes = ['ginger', 'banana', 'tobacco', 'ornamaental', 'rose', 'soyabean', 'papaya', 'garlic',
                        'raspberry', 'mango', 'cotton', 'corn', 'pomgernate', 'strawberry', 'Blueberry', 'brinjal',
                        'potato', 'wheat', 'olive', 'rice', 'lemon', 'cabbage', 'gauava', 'chilli', 'capcicum', 'sunflower',
                        'cherry', 'cassava', 'apple', 'tea', 'sugarcane', 'groundnut', 'weed', 'peach', 'coffee', 'cauliflower',
                        'tomato', 'onion', 'gram', 'chiku', 'jamun', 'castor', 'pea', 'cucumber', 'grape', 'cardamom']
        
        
    def load_health_dt_model(self):
        
        model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=(200, 200, 3)),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        
        Conv2D(64, (3, 3), activation="relu"),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        
        Conv2D(70, (3, 3), activation="relu"),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        
        Conv2D(85, (3, 3), activation="relu"),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        
        Flatten(),
        Dense(512, activation="relu"),
        BatchNormalization(),
        
        Dropout(0.5),
        
        Dense(1, activation="sigmoid")
        
        ])
        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])
        model.load_weights("Health_crop_model.h5")
        
        return model
    
    
    
    def preproccess_img(self):
        img = Image.open(self.image_addr)
        resized = img.resize((200, 200))
        arr_img = np.array(resized)
        arr_img = arr_img.astype('float32') / 255.0 # make pixel values in range of [0, 1] and convert them to float
        arr_img = np.expand_dims(arr_img, axis=0)
        
        return arr_img 

    
    
    def health_detect(self):
        health_dt_model = self.load_health_dt_model()
        predict_model = health_dt_model.predict(self.preproccess_img(), verbose=0)
        get_exact_class = list(self.classes.keys())[round(predict_model[0][0])]
        
        return get_exact_class
    
    
    
    def load_yolo_model(self):
        yolo_model = YOLO('foduucom/plant-leaf-detection-and-classification')

        # set model parameters
        yolo_model.overrides['conf'] = 0.25  # NMS confidence threshold
        yolo_model.overrides['iou'] = 0.45  # NMS IoU threshold
        yolo_model.overrides['agnostic_nms'] = False  # NMS class-agnostic
        yolo_model.overrides['max_det'] = 1000 # maximum number of detections per image
        
        return yolo_model
    
    
    
    def get_leaves_types(self):
        cls_indexes = []
        
        yolo_model = self.load_yolo_model()
        predict_leaves_types = yolo_model.predict(self.image_addr)
        
        render = render_result(model=yolo_model, image=self.image_addr, result=predict_leaves_types[0])
        img_name = f"./leaves_detected/{uuid4()}.jpg"
        render.save(img_name)
        
        for i in range(len(predict_leaves_types[0].boxes)):
            confidence = int(predict_leaves_types[0].boxes[i].conf[0].item()*100)
            if confidence >= 70:
                types = self.leaf_classes[int(predict_leaves_types[0].boxes[i].cls[0].item())]
                cls_indexes.append(f" {types}        %{confidence}")
        
        return cls_indexes, img_name