#pg 69 finger exercise #3, function to test StringContainsAnotherString
import StringContainsAnotherString
def test_is_in (test_1,test_2):
    for word_1 in test_1:
        for word_2 in test_2:
            cont = StringContainsAnotherString.is_in(word_1, word_2)
            if cont:
                does_it = "do"
            else:
                does_it = "do not"
            print(f"The two strings {word_1} and {word_2} {does_it} overlap.")
first_t = ("hello","how","bally")
second_t = ("asashelloiyu","ayhyuow","bazoobally")
test_is_in(first_t,second_t)