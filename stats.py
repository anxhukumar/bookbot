def count_words( book_content ):
  words_list = book_content.split()
  number_of_words = len( words_list )
  return number_of_words

def count_characters( book_content ):
  counter = {}
  for character in book_content:
      character = character.lower()
      if (character in counter):
        counter[character] +=1
      else:
        counter[character] = 1
  return counter