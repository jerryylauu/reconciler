import csv

def parse(spreadsheet):
	content = []
	with open(spreadsheet, newline = '') as csvfile:
		reader = csv.reader(csvfile, delimiter = ' ')
		for row in reader:
			content.append(row)
		return content
			
def 
			
def main():
	spreadsheet1 = parse("MOCK_DATA.csv")
	spreadsheet2 = parse("MOCK_DATA2.csv")
	print(spreadsheet1)
			
if __name__ == '__main__':
	main()