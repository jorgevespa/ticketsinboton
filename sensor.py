import RPi.GPIO as GPIO
import time
import cv2
#Definir el modo GPIO (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#Definir los PINS a utilizar
GPIO_DISPARADOR = 7
GPIO_RESPUESTA = 11
GPIO_LED = 18
 
#Definir el funcionamiento de cada PIN (IN / OUT)
GPIO.setup(GPIO_DISPARADOR, GPIO.OUT)
GPIO.setup(GPIO_RESPUESTA, GPIO.IN)
GPIO.setup(GPIO_LED,GPIO.OUT)

def distancia():
    # Definir disparador como HIGH
    GPIO.output(GPIO_DISPARADOR, True)
 
    # Cambiar el estado del disparador en 0.01ms a LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_DISPARADOR, False)
 
    Inicio = time.time()
    Fin = time.time()
 
    # Guardar Inicio
    while GPIO.input(GPIO_RESPUESTA) == 0:
        Inicio = time.time()
 
    # Guardar el tiempo de respuesta
    while GPIO.input(GPIO_RESPUESTA) == 1:
        Fin = time.time()
 
    # Diferencia de tiempo entre Disparador y Respuesta
    Tiempo = Fin - Inicio
    # Multiplicar por la velocidad Sonica (34300 cm/s)
    # y dividir entre la ida y vuelta
    resultado = (Tiempo * 34300) / 2
 
    return resultado
 
def TomarFoto():
    cam = cv2.VideoCapture(0)
    #cv2.namedWindow("Image_capture_code")
    ret, frame = cam.read()
    #cv2.imshow("Image_capture_code", frame)
    cv2.imwrite('usuario.jpg', frame)
    cam.release()
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    try:
        while True:
            res = distancia()
            if (res <= 10):
                  GPIO.output(GPIO_LED,GPIO.LOW)
                  print ("Distancia = %.1f cm" % res + "--- Imprimir Ticket")
                  TomarFoto()
                  time.sleep(2)
            else:
                  i=0
                  GPIO.output(GPIO_LED,GPIO.HIGH)
                  print ("Distancia = %.1f cm" % res)
                  
            time.sleep(1)
 
        # Salir con CTRL + C
    except KeyboardInterrupt:
        print("Detenido por teclado")
        GPIO.cleanup()
