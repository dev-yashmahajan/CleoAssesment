
def itemizeList(strex, listvals, parentindex = 0):


  if len(listvals) == 1 or type(listvals) == str:
    print(strex + '.' + str(parentindex) + ': ', listvals)
  else:
    idx = 0
    for item in listvals:
      itemizeList(strex, item, str(parentindex) + '.' + str(idx))
      idx += 1
