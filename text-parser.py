def find(substr, infile, outfile):
  with open(infile) as a, open(outfile, 'w') as b:
    for line in a:
      if substr in line:
        b.write(line + '\n')

find('manually', 'test.trc', 'test_output.txt')
