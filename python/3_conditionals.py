am_tired = True
homework_due = False

if am_tired:
  print("I am tired :(")
else:
  print("I am nice and awake!")

if not homework_due:
  print("I did all my homework!")
else:
  print("Homework is still due :(")

if am_tired and homework_due:
  print("I am tired and I have homework due")

if am_tired and not homework_due:
  print("I can go to sleep!")

if not am_tired and homework_due:
  print("Time to do some homework!")