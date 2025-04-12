from stats import count_words, count_characters, sorted_list_of_dictionary
import sys

def main():

  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_content = get_book_text( f"{sys.argv[1]}" )
  num_of_words = count_words( book_content )
  unsorted_dict = count_characters( book_content )
  sorted_list_of_dict = sorted_list_of_dictionary( unsorted_dict )
  
  print( "============ BOOKBOT ============" )
  print( f"Analyzing book found at {sys.argv[1]}..." )
  print( "----------- Word Count ----------" )
  print( f"Found {num_of_words} total words " )
  print( "--------- Character Count -------" )
  
  for item in sorted_list_of_dict:
    if (item[ "character" ].isalpha()):
      print( f"{ item[ "character" ] }: { item[ "count" ] }" )

def get_book_text( file_path ):
  with open( file_path ) as f:
    file_contents = f.read()
    return file_contents

main()
