import cv2

camara = cv2.VideoCapture(0)

while True:

    ret, frame = camara.read()

    if not ret:
        print("No se pudo leer la webcam")
        break

    # La imagen se convierte temporalmente a gris 
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # La imagane gris se convierte a blanco y negro
    umbral, blanco_negro = cv2.threshold(
        gris,
        127,
        255,
        cv2.THRESH_BINARY
    )

    cv2.imshow("Original", frame)
    cv2.imshow("Blanco y Negro", blanco_negro)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camara.release()
cv2.destroyAllWindows()