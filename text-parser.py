
def find(substr, infile, outfile):
    lines = []
    with open(infile) as a, open(outfile, 'a') as b:
        for line in a:
            if substr in line:
                lines.append(line)
                b.write(line + '\n')
    return lines

def parse_text(filepath, substr):
    files = []
    for filename in glob.glob('D:/Illumina/Excludes/*.trc'):
        files.append(filename)

    for item in files:
        find(substr, item, filepath+'/text_output.txt')

# parse_text('D:/Illumina/Excludes','Exclude')
