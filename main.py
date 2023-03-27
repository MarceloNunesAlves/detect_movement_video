import cv2

def analysis_file(path):
    # Carrega o vídeo
    cap = cv2.VideoCapture(path)

    # Frame anterior vazio
    background = None

    has_movement = False
    count_movement = 0

    # Loop principal
    while True:
        # Lê o próximo frame do vídeo
        ret, frame = cap.read()

        # Verifica se o frame foi lido corretamente
        if not ret:
            break

        # Converte o frame para escala de cinza e aplica um filtro Gaussiano
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if background is not None:
            # Subtrai o background do frame atual
            diff = cv2.absdiff(background, gray)
            thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

            # Aplica operações morfológicas para remover ruído
            thresh = cv2.dilate(thresh, None, iterations=2)
            thresh = cv2.erode(thresh, None, iterations=2)

            # Encontra os contornos dos objetos em movimento
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) > 0:
                # Desenha os contornos dos objetos em movimento no frame original
                for contour in contours:
                    # if cv2.contourArea(contour) < 400:
                    #     continue

                    count_movement += 1

                    #if count_movement > 5:
                    has_movement = True

                    print("Tem movimento...")
                    (x, y, w, h) = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                print("Não tem movimento...")

        # Exibe o frame com os contornos dos objetos em movimento
        cv2.imshow('frame', frame)

        # Define o background (Frame anterior)
        background = gray

        # Aguarda 40 milissegundos
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

    # Libera os recursos utilizados
    cap.release()
    cv2.destroyAllWindows()

    return has_movement


if __name__ == '__main__':
    # Video OK
    mov_1 = analysis_file('Video_Com_Pessoa.mp4')

    # Video Sem ngm
    mov_2 = analysis_file('Video_Sem_Ngm.mp4')

    print(f"Movimento 1 {mov_1}")

    print(f"Movimento 2 {mov_2}")