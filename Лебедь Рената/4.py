cv1 = input()
cv2 = input()

r = 'красный'
y = 'желтый'
b = 'синий'

if (cv1 == r) or (cv1 == y) or (cv1 == b):
    if (cv2 == r) or (cv2 == y) or (cv2 == b):
        if cv1 == cv2:
            print('Цвет не изменился')
        if ((cv1 == r) and (cv2 == y)) or ((cv2 == r) and (cv1 == y)):
            print('Цвет: оранжевый')
        if ((cv1 == b) and (cv2 == y)) or ((cv2 == b) and (cv1 == y)):
            print('Цвет: зеленый')
        if ((cv1 == r) and (cv2 == b)) or ((cv2 == r) and (cv1 == b)):
            print('Цвет: фиолетовый')
    else:
        print('Проверьте введенные цвета')
else:
    print('Проверьте введенные цвета')