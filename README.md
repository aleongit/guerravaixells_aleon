# Guerra Vaixells

Exemple del joc de guerra de vaixells amb Python.
Versions OOP (Object-oriented programming) vs Procedimental.

## Requeriments
- python >= 3.8

## Getting Started
- git clone https://github.com/aleongit/guerravaixells_aleon.git
- cd guerravaixells_aleon
- python guerravaixells_aleon.py
- python guerravaixellsoop_aleon.py (OOP)
- play and enjoy ;)


## guerravaixells_aleon.py

```
  A B C D E F G H I J
0 . . . . . . . . . .
1 . . . . . . . . . .
2 . . . . . . . . . .
3 . . . . . . . . . .
4 . . . . . . . . . .
5 . . . . . . . . . .
6 . . . . . . . . . .
7 . . . . . . . . . .
8 . . . . . . . . . .
9 . . . . . . . . . .

5 4 4 3 3 3 2 2
- - - - - - - -

Introdueix la fila 0-9: 0
Introdueix la columna A-J: A
               __   __
              __ \ / __
             /  \ | /  \
                 \|/
            _,.---v---._
   /\__/\  /            \
   \_  _/ /              \
     \ \_|           @ __|
      \                \_
       \     ,__/       /
     ~~~`~~~~~~~~~~~~~~/~~~~
             AIGUA!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Introdueix la fila 0-9: 2
Introdueix la columna A-J: A

             |    |    |
             )_)  )_)  )_)
            )___))___))___)\
          )____)____)_____)\
         _____|____|____|____\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^
   ^^^^     ^^^^     ^^^^     ^^^^
       ^^^^     TOCAT!    ^^^^     ^^^^
---------------------------------------

Introdueix la fila 0-9: 4
Introdueix la columna A-J: C

     _.-^^---....,,--
 _--                  --_
<    B O O O O O O O M   >)
|                         |
 \._                   _./
    ```--. . , ; .--·''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____
===========================
      TOCAT I ENFONSAT
===========================

  A B C D E F G H I J
0 ~ ~ ~ ~ ~ . . # # #
1 ~ . . . ~ ~ . . . .
2 # # # . ~ . ~ . # #
3 ~ . ~ . . ~ # . . .
4 . ~ # ~ . . # . ~ #
5 ~ ~ # . . ~ # ~ . #
6 . . # . ~ . # . . #
7 ~ ~ # . . . ~ . . .
8 # . # ~ . . . . . ~
9 # . ~ . . . . . . .

5 4 4 3 3 3 2 2
# # - # # # # #

Introdueix la fila 0-9: 9
Introdueix la columna A-J: A

       .-'-.            .-'-.            .-'-.           .-'-.
     _/_-.-_\_        _/.-.-.\_        _/.-.-.\_       _/.-.-.\_
    / __} {__ \      /|( o o )|\      ( ( o o ) )     ( ( o o ) )
   / //  ¨  \  \    | //  ¨  \  |      |/  ¨  \|       |/  ¨  \|
  / / \ --- / \ \  / / \ --- / \ \      \`/^\´/         \ --- /
  \ \_/ `'´ \_/ /  \ \_/ `'´ \_/ /      /`\ /´\         / `'´ \
   \           /    \           /      /  /|\  \       /       \
------------------------------------------------------------------
                       JA DESTAPADA!
------------------------------------------------------------------

       _____              __  __   ______        ____   __      __  ______   _____
      / ____|     /\     |  \/  | |  ____|      / __ \  \ \    / / |  ____| |  __ \
     | |  __     /  \    | \  / | | |__        | |  | |  \ \  / /  | |__    | |__) |
     | | |_ |   / /\ \   | |\/| | |  __|       | |  | |   \ \/ /   |  __|   |  _  /
     | |__| |  / ____ \  | |  | | | |____      | |__| |    \  /    | |____  | | \ \
      \_____| /_/    \_\ |_|  |_| |______|      \____/      \/     |______| |_|  \_\


  _____   _   _    _____   ______   _____    _______        _____    ____    _____   _   _
 |_   _| | \ | |  / ____| |  ____| |  __ \  |__   __|      / ____|  / __ \  |_   _| | \ | |
   | |   |  \| | | (___   | |__    | |__) |    | |        | |      | |  | |   | |   |  \| |
   | |   | . ` |  \___ \  |  __|   |  _  /     | |        | |      | |  | |   | |   | . ` |
  _| |_  | |\  |  ____) | | |____  | | \ \     | |        | |____  | |__| |  _| |_  | |\  |
 |_____| |_| \_| |_____/  |______| |_|  \_\    |_|         \_____|  \____/  |_____| |_| \_|

```

## guerravaixellsoop_aleon.py

```
BENVINGUT !!!
____________* JOC J1 *____________

   0  1  2  3  4  5  6  7  8  9
0  .  .  .  .  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .  .
9  .  .  .  .  .  .  .  .  .  .

____________* JOC J1 *____________
POR: 0/1 - CUI: 0/2 - FRA: 0/3 - PAT: 0/4

JOCS => J1=>[0/10]
MENÚ => [FC]Tirada | J[0-9]canvi joc | [+]nou joc | [i]idioma | [x]sortir

TIRA! : 73
TOCAT !!!
ENFONSAT !!!
____________* JOC J1 *____________

   0  1  2  3  4  5  6  7  8  9
0  ~  ~  ~  .  .  .  ~  ~  ~  ~
1  ~  ~  ~  ~  ~  .  .  ~  #  ~
2  .  #  #  #  #  ~  ~  .  #  .
3  .  .  .  .  .  .  #  .  ~  .
4  ~  .  ~  ~  ~  ~  #  ~  .  .
5  ~  .  ~  #  ~  .  #  .  .  .
6  ~  .  .  #  .  .  ~  ~  .  .
7  #  ~  ~  #  .  .  .  ~  .  .
8  ~  .  .  ~  .  .  .  #  #  .
9  ~  #  ~  #  ~  .  .  .  .  ~

____________* JOC J1 *____________
POR: 1/1 - CUI: 2/2 - FRA: 2/3 - PAT: 3/4

JOCS => J1=>[8/10]
MENÚ => [FC]Tirada | J[0-9]canvi joc | [+]nou joc | [i]idioma | [x]sortir

TIRA! :
```