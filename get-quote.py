import fileinput
file_name = 'quotes.txt'
for line in fileinput.FileInput(file_name, inplace=1):
  if 'purity' in line:
    line = line.rstrip()
    line = line.replace(line, line+' and simplicity' + '\n')
  print (line)