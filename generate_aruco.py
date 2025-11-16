import cv2
import numpy as np
import os

# --- Configurazione del Marker ---
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
marker_id = 14
marker_size = 200

# --- Percorso assoluto corretto ---
textures_path = "/home/emanu/rl25_fold/iiwa_ros2/iiwa_description/gazebo/models/aruco_tag/materials/textures"
output_filename = os.path.join(textures_path, "aruco_1.png")

# --- Generazione del Marker ---
marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

# Aggiungi bordo bianco
border_width = 10
final_image = cv2.copyMakeBorder(
    marker_image,
    border_width, border_width,
    border_width, border_width,
    cv2.BORDER_CONSTANT,
    value=[255, 255, 255]
)

# Salva
cv2.imwrite(output_filename, final_image)

print(f"Marker ArUco ID {marker_id} salvato in: {output_filename}")

