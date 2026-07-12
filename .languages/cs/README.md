# Posledni uprava
> jsem zvědavý jak se s tím Github popere


Markdown Cheat Sheet

Praktická pomůcka pro tvorbu dokumentace v Markdownu (GitHub README, návody, poznámky).

⸻

Nadpisy

# Nadpis 1
## Nadpis 2
### Nadpis 3

Výsledek:

Nadpis 1

Nadpis 2

Nadpis 3

⸻

Text

Tučný text

**tučný text**

Výsledek:

tučný text

⸻

Kurzíva

*šikmý text*

Výsledek:

šikmý text

⸻

Tučný + kurzíva

***důležitý text***

Výsledek:

důležitý text

⸻

Seznamy

Nečíslovaný seznam

- položka
- další položka
  - pod položka

Výsledek:

* položka
* další položka
    * pod položka

⸻

Číslovaný seznam

1. První krok
2. Druhý krok
3. Třetí krok

Výsledek:

1. První krok
2. Druhý krok
3. Třetí krok

⸻

Úkoly

- [ ] Nehotovo
- [x] Hotovo

Výsledek:

* Nehotovo
* Hotovo

⸻

Poznámky a upozornění

Citace

> Toto je poznámka.

Výsledek:

Toto je poznámka.

⸻

GitHub Alerts

> [!NOTE]
> Doplňující informace.
> [!TIP]
> Užitečný tip.
> [!IMPORTANT]
> Důležitá informace.
> [!WARNING]
> Pozor na tuto část.
> [!CAUTION]
> Nebezpečná operace.

⸻

Odkazy

[GitHub](https://github.com)

Výsledek:

GitHub

⸻

Obrázky

![Popis obrázku](image.png)

⸻

Kód

Inline kód

Použij příkaz `git pull`.

Výsledek:

Použij příkaz git pull.

⸻

Blok kódu

```bash
git clone https://github.com/user/project.git
```

Výsledek:

git clone https://github.com/user/project.git

Podporované jazyky:

bash
python
javascript
qml
json
yaml
xml
html
css
cpp
csharp

⸻

Tabulky

| Název | Popis |
|---|---|
| QML | UI jazyk |
| Python | Skripty |

Výsledek:

Název	Popis
QML	UI jazyk
Python	Skripty

⸻

Oddělovač

---

Výsledek:

⸻

Emoji

:white_check_mark:
:x:
:warning:
:rocket:

Výsledek:

:white_check_mark:
:x:
:warning:
:rocket:

⸻

HTML v Markdownu

Markdown umožňuje použít HTML.

<div align="center">
Text uprostřed
</div>

⸻

Sbalovací sekce

<details>
<summary>Klikni pro rozbalení</summary>
Skrytý obsah.
</details>

Výsledek:

<details>
<summary>Klikni pro rozbalení</summary>

Skrytý obsah.

</details>

⸻

Klávesy

Stiskni <kbd>Ctrl</kbd> + <kbd>C</kbd>

Výsledek:

Stiskni Ctrl + C

⸻

Badge

![Build](https://img.shields.io/badge/build-passing-green)
![Version](https://img.shields.io/badge/version-1.0-blue)

⸻

Komentář (není vidět)

<!-- Toto GitHub nezobrazí -->

⸻

Escape znaků

Pokud chceš zobrazit Markdown znak:

\*
\#
\_

Výsledek:

*
#
_

⸻

Doporučená struktura README

# Název projektu
Krátký popis projektu.
> [!NOTE]
> Doplňující informace.
> [!TIP]
> Užitečný tip.
## Instalace
```bash
příkaz

Použití

Popis použití.

Funkce

* Funkce 1
* Funkce 2

Stav projektu

* Hotovo
* Plánováno

Licence

Informace o licenci.

---
# Nejčastěji používané prvky
```md
# Nadpis
> [!NOTE]
> Poznámka
> [!TIP]
> Tip
> [!WARNING]
> Varování
- seznam
- [ ] úkol
- [x] hotovo
`kód`
```bash
příkaz

Tabulka	Hodnota

<details>
<summary>Více informací</summary>

Text

</details>
```
:::

Můžeš ho použít jako interní dokumentaci k tvému markdown-localization.yml projektu nebo ho přidat přímo do repozitáře jako pomůcku pro přispěvatele.