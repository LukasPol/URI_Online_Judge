while True:
  try:
    x =input()
    if x == '0':
        print('vai ter copa!')
    else:
        print('vai ter duas!')
  except EOFError:
    break
