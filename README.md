# Kryptografia klucza publicznego

## Wstęp

### Co to jest szyfrowanie?
Najprościej mówiąc, szyfrowanie to proces zabezpieczania informacji, tak aby były zrozumiałe tylko dla uprawnionych.
Służy zachowaniu poufności przesyłanych danych - tylko osoby posiadające specjalny "klucz" mogą odtworzyć oryginalny tekst.
Szyfrując i deszyfrując jakąś informację (to znaczy zamieniając **tekst jawny** na **tekst zaszyfrowany** - **szyfrogram**) posługujemy się odpowiednim **algorytmem** oraz właśnie takim **kluczem**.

### Najprostszy szyfr - szyfr cezara
Jednym z najprostszych i zarazem najstarszych szyfrów (był używany już w starożytności przez Juliusza Cezara w prywatnej korespondencji - stąd jego nazwa) jest **szyfr cezara** (zwany również szyfrem przesuwającym).
Jest rodzajem szyfru podstawieniowego, w którym każda litera zastępowana jest inną, oddaloną od niej o pewną liczbę pozycji w alfabecie. Ta liczba, zwana parametrem przesunięcia pełni tu funkcję klucza.
Na przykład jeżeli parametr przesunięcia wynosi `3`, to każdą literę `A` zastępujemy literą `D`, `B` - `E`, `C` - `F`, itd.  

Jednak złamanie takiego szyfru nie stanowi obecnie żadnego problemu. Z pomocą komputerów można z łatwością łamać szyfry dużo bardziej skomplikowane od szyfru cezara. 

### Współcześnie używany szyfr - AES
Dlatego we współczesnej kryptografii używa się szyfrów o znacznie większym stopniu skomplikowania, na przykład [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) - nowoczesny algorytm szyfrujący, opublikowany w 1998 r. i przyjęty m.in. przez amerykański *National Inistitute of Standards and Technology* (NIST) w 2001 r., który stał się powszechnie używanym standardem.

### Wszystko przez ten Internet...

Zarówno szyfr cezara, jak i AES wymagają, aby nadawca i odbiorca wiadomości posiadali ten sam klucz, za pomocą którego będą szyfrować i odszyfrowywać wymieniane wiadomości. 
Wymaga to wcześniejszego ustalenia wspólnego klucza, w taki sposób, aby nie został on przechwycony. 
Oznacza to, że konieczne jest przekazanie go drogą, co do której mamy pewność, że jest bezpieczna. 
Jeszcze do lat 70. XX wieku nie było to wielkim problemem - klucze można było przekazać drugiej osobie nawet osobiście.  
Jednak w latach 80. i 90., wraz z popularyzacją komputerów i powstaniem Internetu, sytuacja drastycznie się zmieniła. 
Internet nie jest i nigdy nie był bezpiecznym miejscem - przy przesyłaniu przez niego danych ryzyko ich przechwycenia jest bardzo duże. 
Dlatego pojawiła się potrzeba szyfrowania przesyłanych informacji w bezpieczny sposób.  
Jednak tutaj pojawia się problem: trzeba nawiązać komunikację między dwoma urządzeniami, które mogą znajdować się tysiące kilometrów od siebie, w kilka sekund, kiedy jedynym dostępnym środkiem komunikacji jest Internet. 
Wymiana kluczy w bezpieczny sposób nagle nie jest możliwa, a przesłanie ich przez publiczne połączenie generuje potencjalne ryzyko ich przechwycenia.  
Tutaj z pomocą przychodzi kryptografia klucza publicznego.  


## Rodzaje algorytmów kryptograficznych

### Algorytm symetryczny (kryptografia klucza prywatnego)
Algorytm symetryczny do szyfrowaniwa i deszyfrowania wykorzystuje ten sam klucz (lub różne klucze, gdzie jest możliwe wyznaczenie klucza szyfrującego z deszyfrującego i odwrotnie), który powinni znać nadawca i odbiorca zaszyfrowanej wiadomości, ale nikt inny.
Ujawnienie klucza (lub jednego z kluczy) umożliwia odszyfrowanie zaszyfrowanej wiadomości.
Przykładami takich algorytmów są wspomniane wcześniej szyfr cezara i AES.  

### Algorytm asymetryczny (kryptografia klucza publicznego)
Algorytm asymetryczny polega na wykorzystywaniu innego klucza do szyfrowania wiadomości (klucz publiczny) i innego do odszyfrowywania (klucz prywatny). Kryptografia asymetryczna została wynaleziona w latach 70. XX wieku.


## Kryptografia klucza publicznego - sposób działania

### Klucz prywatny i klucz publiczny
Szyfrowanie kluczem publicznym opiera się na tym, że istnieją tak naprawdę dwa klucze: publiczny, służący do szyfrowania wiadomości, i prywatny, który służy do jej odszyfrowania.  
Można sobie to wyobrazić w następujący sposób: klucz publiczny jest kłódką, którą Alicja - odbiorca wiadomości - daje Bobowi - nadawcy (udostępnia publicznie). Klucz prywatny jest kluczem do tej kłódki. W ten sposób, jeżeli Bob chce wysłać wiadomość do Alicji, wystarczy że zamknie swoją wiadomość na tę kłódkę (zaszyfruje ją kluczem publicznym). Jedyną osobą, która będzie w stanie otworzyć kłódkę i odczytać wiadomość, jest Alicja.  

### Jak to działa?
Kryptografia asymetryczna opiera się na funkcjach jednokierunkowych. Są to działania, które łatwo da się wykonać w jedną stronę, a trudno jest wykonać w drugą. Są to na przykład mnożenie (łatwe) i faktoryzacja - rozkład na czynniki (trudne), albo potęgowanie modulo (łatwe) i logarytmowanie dyskretne (trudne).

### Protokół Diffiego-Hellmana (Diffie-Hellman key exchange, DH)
Protokół Diffiego-Hellmana to jeden z pierwszych protokołów klucza publicznego. Nie jest algorytmem szyfrującym - to protokół służący do ustalenia wspólnego tajnego klucza przy użyciu publicznych środków komunikacji. Jego działanie można przedstawić w bardziej zrozumiały sposób za pomocą analogii [mieszania kolorów](images/image_1.png).

1. Alicja i Bob uzgadniają liczbę pierwszą $p$ (np. $23$) i podstawę $g$ (np. $5$).  

2. Alicja wybiera tajną liczbę całkowitą $a$ (np. $6$), i wysyła Bobowi $A = g^{a} \mod p$  
$A = 5^{6} \mod 23$  
$A = 15\ 625 \mod 23$  
$A = 8$  
3. Bob wybiera tajną liczbę całkowitą $b$ (np. $15$), i wysyła Alicji $B = g^{b} \mod p$  
$B = 5^{15} \mod 23$  
$B = 30\ 517\ 578\ 125 \mod 23$  
$B = 19$  
4. Alicja oblicza $s = B^{a} \mod p$, czyli $s = (g^{b})^{a} \mod p$  
$s = 19^{6} \mod 23$  
$s = 47\ 045\ 881 \mod 23$  
$s = 2$  
5. Bob oblicza $s = A^{b} \mod p$, czyli $s = (g^{a})^{b} \mod p$  
$s = 8^{15} \mod 23$  
$s = 35\ 184\ 372\ 088\ 832 \mod 23$  
$s = 2$  
6. Alicja i Bob posiadają wspólną tajną liczbę: $s$ (tutaj: $2$).  
Wynika to z tego, że $(g^{a})^{b} = (g^{b})^{a}$, więc $(g^{a})^{b}$ oraz $(g^{b})^{a}$ są przystające $\mod p$  

Jedynymi wartościami poza $s$ pozostającymi w sekrecie są $a$, $b$ oraz $g^{ab} = g^{ba} \mod p$. Pozostałe wartości są wysyłane jawnie. 

Jeśli ktoś znałby jednocześnie obie tajne wartości $a$ i $b$, to mógłby obliczyć $s$:  
$s = 5^{6 ⋅ 15} \mod 23$  
$s = 5^{15 ⋅ 6} \mod 23$  
$s = 5^{90} \mod 23$  
$s = 807\ 793\ 566\ 946\ 316\ 088\ 741\ 610\ 050\ 849\ 573\ 099\ 185\ 363\ 389\ 551\ 639\ 556\ 884\ 765\ 625 \mod 23$  
$s = 2$   

Dla stosunkowo małych liczb $a$, $b$ i $p$, odgadnięcie $a$ i $b$ poprzez sprawdzenie wszystkich możliwości działania $g^{ab}\mod 23$ nie jest dużym problemem.  
Dlatego, w celu zapewnienia odpowiedniego poziomu bezpieczeństwa, $p$ powinno być liczbą (pierwszą) o długości około 300 cyfr w systemie dziesiętnym, a $a$ i $b$ o długości około 100 cyfr. W ten sposób, nawet przy użyciu ogromnej mocy obliczeniowej, znalezienie $a$ i $b$ w sensownym czasie nie jest możliwe. Ten problem jest znany jako logarytm dyskretny.

