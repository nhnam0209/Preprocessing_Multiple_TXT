import glob
import json
import string
import time
import os
import re
from progress.bar import IncrementalBar
# change input directory and output file name
list_of_files = glob.glob('./example/*.json') 
output_file = "example.txt" #output
output_countWords = "example_countwords.txt" #count number of word
output_pre = "example_done.txt" 
output_pre1 = "example_countwords_done.txt"

def json_to_Text():
    for file_name in list_of_files:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            data = data["content"]
            words = data.strip()
            punc = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
            for ele in words:
                if ele in punc:
                    words = words.replace(ele,"")
            table = str.maketrans("", "", string.punctuation)
            stripped = "".join(w.translate(table) for w in words)
            assembled = "".join(stripped)
        f = open(output_file, "a", encoding='utf-8')
        f.writelines(data + "\n")
        f = open(output_pre, "a", encoding='utf-8')
        f.writelines(assembled+"\n")
        dict1 ={}
        output_pre2 = open("sohoa_completed.json")
        json.dump(dict1, output_pre2, indent=1)
        output_pre2.close()
    print("Complete Extracting.")

def remove_punctuation():
    with open(output_file,"r",encoding="utf-8") as f:
        text = f.read()
        words = text.strip()
        table = str.maketrans(" "," ",string.punctuation)
        stripped = " ".join(w.translate(table) for w in words)
        assembled= " ".join(stripped)
    f = open("sohoa_done.txt","a", encoding = "utf-8")
    f.writelines(assembled+"\n")
    print("Complete Changed.")

def count():
    file = open(output_file, "r", encoding='utf-8')
    number_of_lines = 0
    number_of_words = 0
    number_of_characters = 0
    for line in file:
        line = line.strip("\n")
        words = line.split()
        number_of_lines += 1
        number_of_words += len(words)
        number_of_characters += len(line)
    file.close()
    print("Line count:", number_of_lines)
    print("Word count:", number_of_words)
    print("Character count:", number_of_characters)
    print("-----------------------------------------------")
    print("Extract file location: ")
    print("File Location:" + os.getcwd() + "\\" + output_file)

def countWordsPerLine():
    tupleNum = ()
    with open(output_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(output_countWords, 'w', encoding='utf-8') as f:
        for index, value in enumerate(lines):
            number_of_words = len(value.split())
            f.write('Line number {} has {} words.\n'.format(index + 1, number_of_words))
            tupleNum += (number_of_words,)
            # print(number_of_words)
    # print(tup1)
    minValue = min([x for x in tupleNum if x != 0])
    maxValue = max(tupleNum)
    print("Longest sentence has: ", maxValue, "words")
    print("Shortest sentence has: ", minValue, "words")
def countWordsPerLine1():
    tupleNum = ()
    with open(output_pre, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(output_pre1, 'w', encoding='utf-8') as f:
        for index, value in enumerate(lines):
            number_of_words = len(value.split())
            f.write('Line number {} has {} words.\n'.format(index + 1, number_of_words))
            tupleNum += (number_of_words,)
            # print(number_of_words)
    # print(tup1)
    if number_of_words != 0:
        minValue = min(tupleNum)
        maxValue = max(tupleNum)
        print("Longest sentence has: ", maxValue, "words")
        print("Shortest sentence has: ", minValue, "words")


def main():
    loading_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bar = IncrementalBar('Loading', max=len(loading_number))
    for item in loading_number:
        bar.next()
        time.sleep(1)
    print("\n-----------------------------------------------")
    json_to_Text()
    # remove_punctuation()
    count()
    print("-----------------------------------------------")
    countWordsPerLine()
    print("-----------------------------------------------")
    countWordsPerLine1()
    print("-----------------------------------------------")
    print("Words count file location: ")
    print("File Location:" + os.getcwd() + "\\" + output_countWords)
    print("Complete!.")
    print("-----------------------------------------------")
    bar.finish()
if __name__ == "__main__":
   main()