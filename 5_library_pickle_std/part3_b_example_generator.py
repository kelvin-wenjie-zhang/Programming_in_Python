
# This file is to generate the examples to test the exception
# for part 3 (b)

import sys
import pickle

with open("non_list_message_object", "wb") as f:
  pickle.dump("hello world", f)

outer_list_contain_non_list_element = [[1,1,1],1,[1,1]]
with open("outer_list_contain_non_list_element", "wb") as f:
  pickle.dump(outer_list_contain_non_list_element, f)

too_many_elements_in_inner_list = [[1]*30, [1,1,1,1]]
with open("too_many_elements_in_inner_list", "wb") as f:
  pickle.dump(too_many_elements_in_inner_list, f)
