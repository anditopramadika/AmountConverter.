# Membuat Input Bilangan di terminal 
bil = input('Masukkan bilangan bulat : ')  

# Membuat function def untuk AmountConverter
def AmountConverter(bil):      
    # Menentukan batasan input --> harus bilangan numeric dan tidak lebih dari 359999
    if bil.isnumeric() and 0< int(bil)<= 359999:
    #Konversi bilangan ke rim dengan cara di bagi habis 500 (1 rim = 500 buah)
        rim = int(bil)//500
    #Konversi bilangan ke kodi dikurangi rim dengan cara di mod 500 dan dibagi habis 20 (1 kodi = 20 buah)
        kodi = (int(bil)%500//(20))
    #Konversi bilangan ke lusin dikurangi rim dan kodi dengan cara di mod 500, di mod 20, dan di bagi habis 12 (1 lusin = 12 buah)
        lusin = ((int(bil)%500)%20)//12
        # Print hasil jika memenuhi kriteria batasan
        print('%02d'%rim,':','%02d'%kodi,':','%02d'%lusin)

    else :
        # Jika tidak terpenuhi maka akan print Invalid Input!
        print('Invalid Input!')

# Menjalankan def function AmountConverter
AmountConverter(bil)