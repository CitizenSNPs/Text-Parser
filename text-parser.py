import glob


error_lines = {}

def find(substr, infile, outfile):
    with open(infile) as a, open(outfile, 'a') as b:
        for line in a:
            if substr in line:
                b.write(line + '\n')
                if line not in error_lines:
                    error_lines[line] = 1
                else:
                    error_lines[line] += 1
#files should be trc files of identity match samples
for filename in glob.glob('*.trc'):
    files = []
    files.append(filename)

    for item in files:
        find("error", item, 'test_output.txt')

print error_lines

#"E:P1:08/75" string for manual recovery errors
