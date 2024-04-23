def soal_soal(text):
    with open(text, 'r') as file:
        for line in file:
            soal, jawaban = line.strip().split(' || ')
            print(soal)
            tebakan = input('Jawab: ').lower()
            if tebakan == jawaban.lower():
                print('Jawaban benar!')
            else:
                print('Jawaban salah!')
text=input("masukan file soal: ")
soal_soal(text)