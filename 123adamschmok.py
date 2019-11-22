#   a123_apple_1.py
import turtle as trtl
import random


apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)
wn.bgpic("tree.gif")
#apple = trtl.Turtle()
#drawer = trtl.Turtle()
number_of_apples = 5
current_letters = []
apple_list = []
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = ""
random.shuffle(letter_list)
ground = -150
xcor_offset = -5
ycor_offset = -25
#apple.speed(3)


#apple.pu()
#drawer.pu()
#drawer.ht()
#drawer.goto(0,100)

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  global current_letters
  
  if (len(letter_list) != 0):
    active_apple.shape(apple_image)
    active_apple.goto(random.randint(-200, 200),random.randint(0, 100))
    active_apple.st()
    letter = letter_list.pop()
    draw_letter(letter, active_apple)
    current_letters.append(letter)
    wn.update()

def apple_fall(letter):
  wn.tracer(True)
  index = current_letters.index(letter)
  current_letters.pop(index)
  active_apple = apple_list.pop(index)


  active_apple.clear()
  active_apple.goto(active_apple.xcor(), ground)
  active_apple.ht()
  wn.tracer(False)
  draw_apple(active_apple)
  apple_list.append(active_apple)

def draw_letter(letter, active_apple):
  wn.tracer(False)
  active_apple.color("white")
  old_pos = active_apple.position()
  active_apple.setpos(active_apple.xcor() + xcor_offset, active_apple.ycor() + ycor_offset)
  active_apple.write(letter, font=("arial", 30, "bold"))
  active_apple.setpos(old_pos)

for i in range(number_of_apples):
  active_apple = trtl.Turtle(shape = apple_image)
  active_apple.pu()
  draw_apple(active_apple)
  apple_list.append(active_apple)

#draw_apple(apple)

def test_a ():
  if ("a" in current_letters):
    apple_fall("a")
def test_b ():
  if ("b" in current_letters):
    apple_fall("b")
def test_c ():
  if ("c" in current_letters):
    apple_fall("c")
def test_d ():
  if ("d" in current_letters):
    apple_fall("d")
def test_e ():
  if ("e" in current_letters):
    apple_fall("e")
def test_f ():
  if ("f" in current_letters):
    apple_fall("f")
def test_g ():
  if ("g" in current_letters):
    apple_fall("g")
def test_h ():
  if ("h" in current_letters):
    apple_fall("h")
def test_i ():
  if ("i" in current_letters):
    apple_fall("i")
def test_j ():
  if ("j" in current_letters):
    apple_fall("j")
def test_k ():
  if ("k" in current_letters):
    apple_fall("k")
def test_l ():
  if ("l" in current_letters):
    apple_fall("l")
def test_m ():
  if ("m" in current_letters):
    apple_fall("m")
def test_n ():
  if ("n" in current_letters):
   apple_fall("n")
def test_o ():
  if ("o" in current_letters):
    apple_fall("o")
def test_p ():
  if ("p" in current_letters):
    apple_fall("p")
def test_q ():
  if ("q" in current_letters):
    apple_fall("q")
def test_r ():
  if ("r" in current_letters):
    apple_fall("r")
def test_s ():
  if ("s" in current_letters):
    apple_fall("s")
def test_t ():
  if ("t" in current_letters):
    apple_fall("t")
def test_u ():
  if ("u" in current_letters):
    apple_fall("u")
def test_v ():
  if ("v" in current_letters):
    apple_fall("v")
def test_w ():
  if ("w" in current_letters):
    apple_fall("w")
def test_x ():
  if ("x" in current_letters):
    apple_fall("x")
def test_y ():
  if ("y" in current_letters):
    apple_fall("y")
def test_z ():
  if ("z" in current_letters):
    apple_fall("z")
wn.onkeypress(test_a, "a")
wn.onkeypress(test_b, "b")
wn.onkeypress(test_c, "c")
wn.onkeypress(test_d, "d")
wn.onkeypress(test_e, "e")
wn.onkeypress(test_f, "f")
wn.onkeypress(test_g, "g")
wn.onkeypress(test_h, "h")
wn.onkeypress(test_i, "i")
wn.onkeypress(test_j, "j")
wn.onkeypress(test_k, "k")
wn.onkeypress(test_l, "l")
wn.onkeypress(test_m, "m")
wn.onkeypress(test_n, "n")
wn.onkeypress(test_o, "o")
wn.onkeypress(test_p, "p")
wn.onkeypress(test_q, "q")
wn.onkeypress(test_r, "r")
wn.onkeypress(test_s, "s")
wn.onkeypress(test_t, "t")
wn.onkeypress(test_u, "u")
wn.onkeypress(test_v, "v")
wn.onkeypress(test_w, "w")
wn.onkeypress(test_x, "x")
wn.onkeypress(test_y, "y")
wn.onkeypress(test_z, "z")
wn.listen()



trtl.mainloop()