word = input("Enter your text: ")  # Take user input
asci_list = []   # list to save ascii of chars
new_word = ""
new_word_list = []  # list to save all ordered substring

###########################################
# for loop to convert chars to ascii  #
for char in word:
    asci_list.append(ord(char))
count = 0
i = 0
###########################################

#############################################################################################
# for loop to find long ordered substring by comparing ascii of next char with current char
for num in asci_list:           # loop on all element of chars ascii
    i += 1                      # to always start next loop form next char
    for sec in asci_list[i:]:
                                # sec is ascii of next char # num is ascii of current char
        if sec >= num:          # this condition means that 2 chars is ordered
            if count == 0:      # if 2 chars is first to chars in ordered substring
                count += 1
                new_word = chr(num) + chr(sec)    # concatenate 2 chars together in one string
            else:                                 # if they are not first 2 ordered chars in this substring or if there are previous ordered chars
                count += 1
                new_word = new_word + chr(sec)    # concatenate next ordered char to previous ordered substring
            break
        else:                           # if Sec is not in order with num
            if count == 0:              # this may carry 2 meaning
                                        # / first : that we are in the beginning of the loop
                                        # and second char is not in order with first one
                                        # / second : we are in any where and this second char in sequence
                                        # that is not in order and we are coming from next else and that is why count is 0
                new_word = chr(num)     # because of second char is not in order with first one ,so put first one in separate substring
                new_word_list.append(new_word)   # append to new substring list
            else:
                new_word_list.append(new_word)   # here we are coming from 2 or more in order chars and next char is not in order with them
                new_word = chr(sec)              #start new substring
                count = 0                        # make counter 0 to start new ordered substring
            break
    if count == 0:             # if last char if string is not ordered with previous
        new_word = chr(num)    # append it in separate substring

new_word_list.append(new_word)  # After finish loops append non-appended substring
####################################################################################

#########################################################
# check the longest substring
longest = new_word_list[0]
for element in new_word_list:
    if len(element) > len(longest):
        longest = element
#########################################################

print(f'All : {new_word_list} ::  Longest : {longest}')
