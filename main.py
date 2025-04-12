from stats import count_words, count_characters

def main():
  book_content = get_book_text( "./books/frankenstein.txt" )
  num_of_words = count_words( book_content )
  print(f"{num_of_words} words found in the document")
  num_of_characters = count_characters( book_content )
  print(num_of_characters)

def get_book_text( file_path ):
  with open( file_path ) as f:
    file_contents = f.read()
    return file_contents

main()
