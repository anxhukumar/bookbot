def count_words( book_content ):
  words_list = book_content.split()
  number_of_words = len( words_list )
  
  return number_of_words

def count_characters( book_content ):
  counter = {}
  
  for character in book_content:
      character = character.lower()
      if character in counter:
        counter[ character ] +=1
      else:
        counter[ character ] = 1
  
  return counter

def sorted_list_of_dictionary( dict ):
  sorted_counter_dict_list = []
  
  for character in dict:
    new_dict = {
      'character': character,
      'count': dict[ character ]
    }
    sorted_counter_dict_list.append( new_dict )
  
  def sort_on( dictionary ):
    return dictionary[ "count" ]
  
  sorted_counter_dict_list.sort( reverse=True, key=sort_on )
  
  return sorted_counter_dict_list
