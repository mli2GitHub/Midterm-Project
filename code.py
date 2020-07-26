points = 0

print("This is a Would - You - Rather - like game. Choose a letter and see if your choice was popular or unpopular.")

def input_(prompt,ans1,ans2):
    global points
    while True:
        input__=input(prompt).lower()
        if input__ == ans1:
            print("Popular!")
            points += 1
            break
        elif input__ == ans2:
            print("Unpopular")
            break
        else:
            print("...")

input_("Cats (c) or Dogs (d)? ", "d", "c")

input_("Toilet Paper Under (u) or Toilet Paper Over (o)? ", "o", "u")

input_("Wii (W) or Xbox (X)? ", "w", "x")

if points == 3:
  input("You are totally in the mainstream!")
elif points == 2:
  input("You've got one outlier, but that's completely fine!")
else:
  input("You wanted to avoid the mainstream, huh?")
