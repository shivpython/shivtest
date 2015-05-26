#Ans 1.
import itertools
def rotate_array(inpt_array, rotate_by):
    for each in xrange(rotate_by):
        popelmnt = inpt_array.pop(-1)
        inpt_array.insert(0,popelmnt)
    return inpt_array
    
inpt_array = [1,2,3,4,5,6]
rotate_by = 2
print 'rotateby', rotate_array(inpt_array, rotate_by)

#Ans2.
#a. “0” == 0 #true both operand conerted to string
#b. “” == 0  #true  Reason: In this the left operand is changed  to the type Number
#c. “” == “0” #false non empty string is true and empty string is false

#Ans 3.
arry_string = ['debca', 'debca', 'abcfgde', 'bca', 'acbd']
print sorted(arry_string, key=len)

#Ans4. value of final_answer is 16

#Ans 5.
def decode_inputs(ciphertxt, shiftby):
    ''' (str, int) -> str
    Shift every letter in the code by the integer 'shiftby 3'.
    '''
    decipher = ''
    for char in ciphertxt:
        
        if 65<=ord(char)<=90:
            decipher = decipher + chr((ord(char) - 65 + shiftby)%26+65)
        if 97<=ord(char)<=122:
            decipher = decipher + chr((ord(char) - 97 + shiftby)%26+97)
        else:
            decipher += char
    return decipher
print 'caesar', decode_inputs('Vrphwklqj phdqlqixo', 3)

#Ans 6.    
print 'caesar', decode_inputs('''Zulwh d surjudp (lq Sbwkrq, MdydVfulsw ru Uxeb) wr srsxodwh dqg wkhq vruw d
udqgrpob glvwulexwhg olvw ri 1 ploolrq lqwhjhuv, hdfk lqwhjhu kdylqj d ydoxh >= 1 dqg
<= 100.
Brxu surjudp vkrxog fduhixoob frqvlghu wkh lqsxw dqg frph xs zlwk wkh prvw hiilflhqw
vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu
dojrulwkp''', 3)
