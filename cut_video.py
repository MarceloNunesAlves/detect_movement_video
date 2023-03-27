import cv2
# Carrega o vídeo
cap = cv2.VideoCapture('[Nome do arquivo para cortar].mp4')

frame_rate = 1
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Inicializa o objeto VideoWriter para escrever o vídeo em mp4
out = cv2.VideoWriter('XXXX.mp4', fourcc, frame_rate, (frame_width, frame_height))

count = 0
# Loop principal
while True:
    # Lê o próximo frame do vídeo
    ret, frame = cap.read()

    if ret:
        count += 1
        if count < 240:
            continue

        # Adiciona o frame ao objeto VideoWriter
        out.write(frame)

    else:
        # Encerra o loop quando não há mais frames
        break

# Libera os recursos
out.release()
cap.release()