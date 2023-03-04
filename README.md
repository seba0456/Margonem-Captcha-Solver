# Margonem-Captcha-Solver
Model wytrenowany do wskazywania obrazków captcha, na których występują artefakty.
## Ograniczenia
Na chwilę obecną model nie znajduje praktycznego zastosowania i służy jedynie jako program, który potrafi stwierdzić obecność linii na obrazku. Jego skuteczność oscyluje między 70 a 90 procentami. Warto podkreślić, że program nie pobiera obrazków bezpośrednio z gry Margonem, a konieczne jest dostarczenie go z zewnątrz.
## Po co ten program?
Program ten został stworzony w celu nauki maszynowego uczenia i wydaje się jedynie miłą ciekawostką. Jednym z możliwych kierunków dalszego rozwoju programu jest nauczenie go rozpoznawania liter, co pozwoliłoby na zwrócenie informacji na temat odpowiadających im obrazków. Można również pójść o krok dalej i zaimplementować funkcjonalność przechwytywania obrazów z przeglądarki, dzielenia ich na mniejsze fragmenty i przekazywania ich do modelu, który mógłby wskaźć, które obrazy zawierają artefakty, a które są czyste. W ten sposób, dodając trochę instrukcji warunkowych, program mógłby być użyty do automatycznego wybierania odpowiednich opcji za pomocą kursora.

Niestety, w pierwotnej wersji programu występują pewne ograniczenia, takie jak konieczność ręcznego dostarczania obrazków do modelu oraz jego niskie skuteczności w rozpoznawaniu artefaktów (70-90%). Jednakże, mimo tych ograniczeń, program może stanowić ciekawe narzędzie edukacyjne. 

Niestety, nie jestem w stanie określić, czy program będzie przezemnie rozwijany, ja na ten moment uważam ten program za ciekawostkę.

# Jak używać?
Na ten moment należy wyciąć obrazek z menu zagadki oraz nazwać go tester.png, a następnie umieścić go w tym samym folderze co `tester.py`. Program odpalamy za pomocą polecenia w termianlu `python tester.py`. Następnie program zwróci nam do której kategorii porawdopodobnie należy obrazek. 

Poniżej daje przykład takiego obrazka:

![Przykład obrazka](https://i.imgur.com/xZ00jIy.png)
![Przykład obrazka](https://i.imgur.com/fOXQcE0.png)

Miej na uwadze, że model **nie jest nieomylny!**
