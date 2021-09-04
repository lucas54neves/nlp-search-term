import sys
import glob

def read_file(file_path):
     with open(file_path, 'r') as reader:
        return reader.read()

def pre_processing(content):
    content_as_lower = content.lower()

    pre_processed_content = ''

    for letter in content_as_lower:
        if letter not in '\!\"\#\$\%\&\\\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\\\]\^\_\`\{\|\}\~':
            pre_processed_content += letter
    
    return pre_processed_content

def tokenize(text):
    return text.split()

def calculate_overlap(list1, list2):
    sum_of_common_tokens = 0

    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                sum_of_common_tokens += 1
    
    return sum_of_common_tokens / max(len(list1), len(list2))

def main():
    directory_path = sys.argv[1]

    search_string = sys.argv[2]

    list_of_files = glob.glob(f'{directory_path}/*.txt')

    overlaps = []

    contents = []

    pre_processed_search = pre_processing(search_string)

    tokenized_search = tokenize(pre_processed_search)

    for file in list_of_files:
        content = read_file(file)

        contents.append(content)

        pre_processed_content = pre_processing(content)

        tokenized_content = tokenize(pre_processed_content)

        overlap = calculate_overlap(tokenized_search, tokenized_content)

        overlaps.append(overlap)

    max_index = 0

    max_overlap = overlaps[max_index]

    for index, element in enumerate(overlaps):
        if element > max_overlap:
            max_index = index

            max_overlap = element

    print(contents[max_index])

main()