#Tapsiriq 3
age = int(input("Yaşınızı daxil edin: "))

if age < 18:
    print("Giriş qadağandır")
else:
    print("Xoş gəldiniz!")

##################################################################

score1 = int(input("1-ci imtahan balinizi yazin: "))
score2 = int(input("2-ci imtahan balinizi yazin: "))
score3 = int(input("3-cu imtahan balinizi yazin: "))

average_score = (score1 + score2 + score3) / 3

if average_score > 90:
    print("Əla!")
elif average_score >= 70:
    print("Yaxşı")
elif average_score >= 50:
    print("Kafi")
else:
    print("Zəif")

########################################################################

age = int(input("Yasinizi daxil edin: "))
score = int(input("İmtahan balinizi daxil edin: "))

if age > 18 and score > 70:
    print("Tebrikler, siz sertlere uygunsuz!")
else:
    print("Siz, şertlere uygun deyilsiniz.")

if age > 18 or score > 90:
    print("En azı bir serti kecdiniz!")
else:
    print("Hec bir serti kecmediniz.")

if not age < 13:
    print("Siz 13 yasdan yuxarısınız.")
else:
    print("Siz 13 yasdan kiciksiniz.")
