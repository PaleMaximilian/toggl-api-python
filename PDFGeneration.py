

def generatePDF(content, output):
    with open('./' + output + '.pdf', 'wb') as f:
            f.write(content)