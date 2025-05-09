# Python Turtle – Eine umfassende Einführung für Einsteiger

Dieses README richtet sich an alle, die Python lernen und auf spielerische Weise erste Grafiken und Programme erstellen möchten. Mit dem Modul **turtle** lassen sich in wenigen Schritten bunte Zeichnungen, Formen und sogar kleine Spiele umsetzen.

---

## Inhaltsverzeichnis

1. [Warum Python Turtle?](#warum-python-turtle)  
2. [Installation und Setup](#installation-und-setup)  
3. [Grundlegende Konzepte](#grundlegende-konzepte)  
4. [Erstes Turtle-Programm](#erstes-turtle-programm)  
5. [Zeichen- und Bewegungskommandos](#zeichen--und-bewegungskommandos)  
6. [Schleifen und Muster](#schleifen-und-muster)  
7. [Funktionen und Modularisierung](#funktionen-und-modularisierung)  
8. [Farb- und Stifteleinstellungen](#farb--und-stifteleinstellungen)  
9. [Ereignis- und Maus-Interaktion](#ereignis--und-maus-interaktion)  
10. [Fortgeschrittene Beispiele](#fortgeschrittene-beispiele)  
11. [Projektideen](#projektideen)  
12. [Tipps & Tricks](#tipps--tricks)  
13. [Weiterführende Ressourcen](#weiterf%C3%BChrende-ressourcen)

---

## Warum Python Turtle?

- **Sofortiges visuelles Feedback**  
  Jeder Befehl führt zu einer sichtbaren Änderung im Zeichenfenster. So siehst du direkt, was dein Code bewirkt – ideal für motivierendes Lernen.
- **Einfacher Einstieg**  
  Die API beschränkt sich auf wenige, leicht verständliche Befehle (z. B. `forward()`, `left()`, `circle()`). Perfekt für Programmier-Neulinge.
- **Lernpfad zu klassischen Konzepten**  
  Turtle-Programme behandeln grundlegende Themen wie Variablen, Schleifen, Funktionen, Bedingungen und Ereignisse.
- **Keine zusätzliche Software nötig**  
  Turtle ist in der Standard-Python-Bibliothek enthalten und läuft auf Windows, macOS und Linux.

---

## Installation und Setup

1. **Python-Version prüfen**  
   Turtle ist ab Python 3.x enthalten. Prüfe deine Version mit:
   ```bash
   python3 --version
   ```
2. **Turtle importieren**  
   In einem neuen Python-Skript genügt:
   ```python
   import turtle
   ```
3. **Bei Bedarf Nachinstallation**  
   Falls du eine spezielle Distribution (z. B. MicroPython) nutzt und Turtle fehlt, kannst du es nachinstallieren:
   ```bash
   pip install PythonTurtle
   ```

---

## Grundlegende Konzepte

- **Turtle-Fenster** (`Screen`)  
  Erzeugt das Zeichenfenster, in dem alle Grafiken angezeigt werden.
- **Turtle-Objekt** (`Turtle`)  
  Der „Stift“ bzw. die „Schildkröte“, die sich im Fenster bewegt und Zeichnungen erzeugt.
- **Stift absenken/aufrichten** (`pendown()`, `penup()`)  
  Bestimmt, ob Bewegungen Linien zeichnen oder nicht.
- **Zeichenattribute**: Farbe, Linienstärke, Form

---

## Erstes Turtle-Programm

```python
import turtle

# Fenster erstellen
screen = turtle.Screen()
screen.title("Mein erstes Turtle-Programm")

# Turtle erzeugen
t = turtle.Turtle()
t.shape("turtle")      # Form der Schildkröte
t.color("green")       # Stift- und Füllfarbe
t.pensize(3)           # Linienstärke

# Bewegung
t.forward(100)         # 100 Pixel vorwärts
t.left(90)             # 90° nach links drehen
t.forward(100)

# Fenster offen halten
screen.mainloop()
```

---

## Zeichen- und Bewegungskommandos

| Befehl                | Wirkung                                           |
|-----------------------|---------------------------------------------------|
| `forward(d)` / `fd(d)`| Bewegt sich d Pixel vorwärts                     |
| `backward(d)` / `bk(d)`| Bewegt sich d Pixel rückwärts                   |
| `right(a)` / `rt(a)`  | Drehung um a Grad im Uhrzeigersinn               |
| `left(a)` / `lt(a)`   | Drehung um a Grad gegen den Uhrzeigersinn        |
| `penup()` / `pu()`    | Stift anheben (kein Zeichnen)                    |
| `pendown()` / `pd()`  | Stift absenken (zeichnen aktiv)                  |
| `goto(x, y)`          | Springt zur Position (x, y)                      |
| `circle(r)`           | Zeichnet einen Kreis mit Radius r                |

---

## Schleifen und Muster

```python
for _ in range(36):
    t.forward(200)
    t.right(170)
```

Dieses kurze Programm erzeugt eine schöne Stern-/Spiralform durch wiederholte Drehung.

---

## Funktionen und Modularisierung

```python
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

for size in [50, 100, 150]:
    draw_square(size)
    t.penup()
    t.forward(200)
    t.pendown()
```

---

## Farb- und Stifteleinstellungen

```python
t.color("blue", "lightblue")     # Stift- und Füllfarbe
t.pensize(5)                     # Linienstärke
t.fillcolor("yellow")            # Nur Füllfarbe
t.begin_fill()
t.circle(50)
t.end_fill()
```

---

## Ereignis- und Maus-Interaktion

```python
def go_forward():
    t.forward(50)

screen.listen()
screen.onkey(go_forward, "Up")   # Pfeil-hoch bewegt die Schildkröte
screen.mainloop()
```

---

## Fortgeschrittene Beispiele

- **Spiralen und Fraktale**: Zeichne das berühmte Barnsley-Fraktal oder einfache Spiralen.  
- **Zeichen-Apps**: Erlaube dem Benutzer, per Mausfüllungen oder Freihandzeichnungen zu erstellen.  
- **Minispiele**: Baue einen kleinen „Turtle“-Racer, bei dem zwei Schildkröten gegeneinander laufen.  

---

## Projektideen

1. **Regenbogen-Spirale**: Verwende eine Farbpalette und Schleifen, um eine mehrfarbige Spirale zu zeichnen.  
2. **Paint-Programm**: Klick-Events nutzen, um an der Klickposition Punkte oder Linien zu zeichnen.  
3. **Labyrinth-Generator**: Erzeuge per Algorithmus ein Labyrinth und lasse die Turtle es automatisch lösen.  

---

## Tipps & Tricks

- Experimentiere mit **Wartezeiten**: `turtle.sleep(0.5)` für langsame Animationen.  
- Nutze `speed(n)`, um die Zeichengeschwindigkeit anzupassen.  
- Verstecke die Turtle mit `hideturtle()`, wenn nur das Bild zählen soll.  
- Speichere Screenshots deines Fensters mit `getcanvas().postscript(file="bild.ps")`.  

---

## Weiterführende Ressourcen

- 📘 Offizielle Dokumentation  
  https://docs.python.org/3/library/turtle.html  
- 🌐 Tutorials & Beispiele  
  - [Real Python – Turtle Graphics](https://realpython.com/beginners-guide-python-turtle/)  
  - [Programiz – Python Turtle](https://www.programiz.com/python-programming/turtle)  
- 🎥 Video-Kurse auf YouTube (Stichwort „Python Turtle Tutorial")  

---

Viel Erfolg und vor allem Spaß beim Experimentieren mit **Python Turtle**! 🚀
