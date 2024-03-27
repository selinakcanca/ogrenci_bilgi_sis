from school import Student, Teacher
öğrenci1 = Student("Elif", "Demir", "True", "10A")
öğrenci1.notEkle(80, 90)
print(öğrenci1.öğrenciBilgi())

öğretmen = Teacher("Ahmet Yilmaz")
öğretmen.kanaatNotuEkle(öğrenci1, 5)

öğrenci2 = Student("Enes", "Çetin", "True", "5B")
öğrenci2.notEkle(73, 88)
print(öğrenci2.öğrenciBilgi())

öğretmen = Teacher("Büşra Haciosmanoğlu")
öğretmen.kanaatNotuEkle(öğrenci2, 10)
