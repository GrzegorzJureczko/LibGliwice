from library import models


def add_to_libraries():
    # zapełnia tabelę libraries danymi bibliotek
    bc = models.Libraries(
        name='Biblioteka Centralna',
        short_name='BC',
        address='ul. Kościuszki 17',
        phone='32 231 54 05',
        email='bc@biblioteka.gliwice.pl',
        opening_time='poniedziałek 8:00 – 20:00, wtorek 8:00 – 20:00, środa 8:00 – 20:00, czwartek 8:00 – 20:00, piątek 8:00 – 20:00, sobota 8:00 – 15:00'
    )
    bc.save()

    bf = models.Libraries(
        name='Biblioforum',
        short_name='BF',
        address='ul. Lipowa 1',
        phone='500 550 772',
        email='bf@biblioteka.gliwice.pl',
        opening_time='poniedziałek 9:00 – 20:00, wtorek 9:00 – 20:00, środa 9:00 – 20:00, czwartek 9:00 – 20:00, piątek 9:00 – 20:00, sobota 9:00 – 20:00'
    )
    bf.save()

    f1 = models.Libraries(
        name='Filia nr 1',
        short_name='F1',
        address='pl. Inwalidów Wojennych 3',
        phone='32 231 97 54',
        email='filia1@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00v'
    )
    f1.save()

    f5 = models.Libraries(
        name='Filia nr 5',
        short_name='F5',
        address='ul. Perkoza 12',
        phone='32 232 13 35',
        email='filia5@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00'
    )
    f5.save()

    f6 = models.Libraries(
        name='Filia nr 6',
        short_name='F6',
        address='ul. Perłowa 17',
        phone='32 301 20 09',
        email='filia6@biblioteka.gliwice.pl',
        opening_time='poniedziałek 15:30 – 19:00, wtorek nieczynna, środa 15:30 – 19:00, czwartek 9:00 – 15:00, piątek 15:30 – 19:00, sobota nieczynna'
    )
    f6.save()

    f7 = models.Libraries(
        name='Filia nr 7',
        short_name='F7',
        address='ul. Junaków 4',
        phone='32 230 07 40',
        email='filia7@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00'
    )
    f7.save()

    f9 = models.Libraries(
        name='Filia nr 9',
        short_name='F9',
        address='ul. Czwartaków 18',
        phone='32 238 39 43',
        email='filia9@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00'
    )
    f9.save()

    f11 = models.Libraries(
        name='Filia nr 11',
        short_name='F11',
        address='ul. bł. Czesława 24',
        phone='32 231 85 53',
        email='filia11@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 11:00 – 15:00, piątek 11:00 – 19:00, sobota nieczynna'
    )
    f11.save()

    f13 = models.Libraries(
        name='Filia nr 13',
        short_name='F13',
        address='ul. Paderewskiego 56',
        phone='32 279 95 82',
        email='filia13@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00'
    )
    f13.save()

    f15 = models.Libraries(
        name='Filia nr 15',
        short_name='F15',
        address='ul. Piastowska 3',
        phone='32 230 19 58',
        email='filia15@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 11:00 – 15:00, piątek 11:00 – 19:00, sobota nieczynna'
    )
    f15.save()

    f16 = models.Libraries(
        name='Filia nr 16',
        short_name='F16',
        address='ul. Przedwiośnie 2',
        phone='32 237 07 23',
        email='filia16@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00'
    )
    f16.save()

    f17 = models.Libraries(
        name='Filia nr 17',
        short_name='F17',
        address='ul. Spółdzielcza 33a',
        phone='32 270 22 65',
        email='filia17@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00'
    )
    f17.save()

    f20 = models.Libraries(
        name='Filia nr 20',
        short_name='F20',
        address='ul. Bernardyńska 2',
        phone='32 279 35 33',
        email='filia20@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00'
    )
    f20.save()

    f21 = models.Libraries(
        name='Filia nr 21',
        short_name='F21',
        address='ul. Syriusza 30',
        phone='32 238 10 05',
        email='filia21@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00'
    )
    f21.save()

    f22 = models.Libraries(
        name='Filia nr 22',
        short_name='F22',
        address='ul. Spacerowa 6',
        phone='32 301 02 40',
        email='filia22@biblioteka.gliwice.pl',
        opening_time='poniedziałek nieczynna, wtorek 8:00 – 15:00, środa 13:00 – 19:00, czwartek 11:00 – 15:00, piątek nieczynna, sobota nieczynna'
    )
    f22.save()

    f23 = models.Libraries(
        name='Filia nr 23',
        short_name='F23',
        address='ul. Sopocka 2',
        phone='32 301 50 92',
        email='filia23@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek nieczynna, środa 8:00 – 12:00, czwartek nieczynna, piątek 11:00 – 19:00, sobota nieczynna'
    )
    f23.save()

    f24 = models.Libraries(
        name='Filia nr 24',
        short_name='F24',
        address='ul. Architektów 109',
        phone='32 301 10 34',
        email='filia24@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek nieczynna, środa 11:00 – 19:00, czwartek nieczynna, piątek 11:00 – 19:00, sobota nieczynna'
    )
    f24.save()

    f25 = models.Libraries(
        name='Filia nr 25',
        short_name='F25',
        address='ul. Jaśminu 20',
        phone='32 300 94 80',
        email='filia25@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek nieczynna, środa 11:00 – 19:00, czwartek nieczynna, piątek 11:00 – 19:00, sobota nieczynna'
    )
    f25.save()

    f30 = models.Libraries(
        name='Filia nr 30',
        short_name='F30',
        address='ul. Partyzantów 25',
        phone='32 557 70 15',
        email='filia30@biblioteka.gliwice.pl',
        opening_time='poniedziałek 11:00 – 19:00, wtorek 8:00 – 15:00, środa 11:00 – 19:00, czwartek 8:00 – 15:00, piątek 11:00 – 19:00, sobota 8:00 – 15:00'
    )
    f30.save()


    print('zapisano dane bibliotek w bazie danych')
