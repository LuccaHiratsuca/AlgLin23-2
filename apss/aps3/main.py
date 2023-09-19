import numpy as np
import cv2 as cv
from functions import *

def run():
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FPS, 45)

    width = 500
    height = 300

    angulo = 0
    scale = 1

    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # Inicializar variáveis para gravação de vídeo
    recording = False
    fourcc = cv.VideoWriter_fourcc(*'H264')  # Usar o codec H264 para MP4
    out = None

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Não consegui capturar frame!")
            break

        frame = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
        image = np.array(frame).astype(float) / 255

        # Aplicar a transformação à imagem
        image_transformada = transform(image, angulo, scale)

        # Ao clicar q, sair do loop
        if cv.waitKey(1) == ord('q'):
            break

        # Direita
        elif cv.waitKey(1) == ord('d'):
            angulo += 3

        # Esquerda
        elif cv.waitKey(1) == ord('a'):
            angulo -= 3

        # Zoom in
        elif cv.waitKey(1) == ord('z'):
            scale += 0.1

        # Zoom out
        elif cv.waitKey(1) == ord('x'):
            scale -= 0.1

        # Gravar vídeo
        elif cv.waitKey(1) == ord('s'):
            if not recording:
                # Iniciar gravação de vídeo
                recording = True
                out = cv.VideoWriter('video.mp4', fourcc, 20, (width, height))

        # Parar gravação de vídeo e salvar
        elif cv.waitKey(1) == ord('e'):
            if recording:
                # Parar gravação de vídeo
                recording = False
                if out is not None:
                    out.release()
                    print("Vídeo salvo como 'video.mp4'")

        if recording:
            # Gravar o frame atual no vídeo
            if out is not None:
                out.write((image_transformada * 255).astype(np.uint8))

        cv.imshow('Minha Imagem!', image_transformada)

    cap.release()
    cv.destroyAllWindows() # CUIDADO! Isso fecha todas as janelas abertas pelo OpenCV

run()
