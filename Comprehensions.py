import csv
import string

def main():
    counts = {}
    words = get_words('address.txt')

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts, 'counts.csv')



def get_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        translator = str.maketrans('', '', string.punctuation)
        processed_content = content.translate(translator)
        word_list = processed_content.split()
        return word_list
    
def save_counts(counts, output_file_path):
    with open(output_file_path, 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(['Word', 'Count'])

        for word, count in counts.items():
            writer.writerow([word, count])


    
main()