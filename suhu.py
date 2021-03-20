def option():
    print("Pilih salah satu dari tiga fungsionalitas berikut:")
    print("1. Konversi suhu C-R")
    print("2. Konversi suhu C-F")
    print("3. Keluar dari program")
    pilihan = int(input("Masukkan pilihan Anda (1/2/3):"))
    return pilihan

def konversi_reamur():
	celcius = int(input("Masukkan suhu dalam celcius: "))
	reamur = (4/5)*celcius
	return reamur

def konversi_farenheit():
	celcius = int(input("Masukkan suhu dalam celcius: "))
	farenheit = (9/5)*celcius+32
	return farenheit

pilihan = option()

while(pilihan > 0):
	pilihan = option()
	if(pilihan==1):
		print("Hasil konversi reamur adalah",(konversi_reamur()))
	elif(pilihan==2):
		print("Hasil konversi farenheit adalah",(konversi_farenheit()))
	elif (pilihan==3):
		print("Goodbye")
		break;