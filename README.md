# Kryptografia klucza publicznego

## Krótki wstęp

### Co to jest szyfrowanie?
Najprościej mówiąc, szyfrowanie to proces zabezpieczania informacji, tak aby były zrozumiałe tylko dla uprawnionych.
Służy zachowaniu poufności przesyłanych danych - tylko osoby posiadające specjalny "klucz" mogą odtworzyć oryginalny tekst.
Szyfrując i deszyfrując jakąś informację (to znaczy zamieniając **tekst jawny** na **tekst zaszyfrowany** - **szyfrogram**) posługujemy się odpowiednim **algorytmem** oraz właśnie takim **kluczem**.

### Najprostszy szyfr - szyfr cezara
Jednym z najprostszych i zarazem najstarszych szyfrów (był używany już w starożytności przez Juliusza Cezara w prywatnej korespondencji - stąd jego nazwa) jest **szyfr cezara** (zwany również szyfrem przesuwającym).
Jest rodzajem szyfru podstawieniowego, w którym każda litera zastępowana jest inną, oddaloną od niej o pewną liczbę pozycji w alfabecie. Ta liczba, zwana parametrem przesunięcia pełni tu funkcję klucza.
Na przykład jeżeli parametr przesunięcia wynosi `3`, to każdą literę `A` zastępujemy literą `D`, `B` - `E`, `C` - `F`, itd.  

Jednak złamanie takiego szyfru nie stanowi obecnie żadnego problemu. Z pomocą komputerów można z łatwością łamać szyfry dużo bardziej skomplikowane od szyfru cezara. Dlatego we współczesnej kryptografii używa się szyfrów o znacznie większym stopniu skomplikowania, na przykład [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) - nowoczesny algorytm szyfrujący, opublikowany w 1998 r. i przyjęty m.in. przez amerykański *National Inistitute of Standards and Technology* (NIST) w 2001 r., który stał się powszechnie stosowanym standardem.

## Rodzaje algorytmów kryptograficznych
Zarówno szyfr cezara, jak i AES wymagają, aby nadawca i odbiorca wiadomości posiadali ten sam klucz, za pomocą którego będą szyfrować i odszyfrowywać wymieniane wiadomości. 
Wymaga to wcześniejszego ustalenia wspólnego klucza, w taki sposób, aby nie został on przechwycony. Oznacza to, że konieczne jest przekazanie go drogą, co do której mamy pewność, że jest bezpieczna. 
Jeszcze do lat 70. XX wieku nie było to wielkim problemem - klucze można było przekazać drugiej osobie na przykład osobiście.  
Jednak w latach 80. i 90., wraz z popularyzacją komercyjnych komputerów i powstaniem Internetu, sytuacja drastycznie się zmieniła. Internet nie jest i nigdy nie był bezpiecznym miejscem - przy przesyłaniu przez niego danych ryzyko ich przechwycenia jest bardzo duże. Dlatego pojawiła się potrzeba bezpiecznego szyfrowania przesyłanych informacji.  
Jednak tutaj pojawia się problem: trzeba nawiązać komunikację między dwoma urządzeniami, które mogą znajdować się tysiące kilometrów od siebie, w kilka sekund, kiedy jedynym dostępnym środkiem komunikacji jest Internet. Wymiana kluczy w bezpieczny sposób nagle nie jest możliwa, a przesłanie ich przez publiczne połączenie generuje potencjalne ryzyko ich przechwycenia.

