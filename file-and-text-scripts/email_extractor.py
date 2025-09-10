#Email Extractor , Script 13. From a given text, extract words with @.
# username@domain.extension
text="hello, this is vinod. my email is vinod@fun.com  " \
"and my friends email is friend@fun.com , " \
"my brother also has email vinod_bro@family.co.uk"
# importing regex module.
import re
reg=re.findall(r"[A-Za-z0-9_%+-.]+" 
               r"@[A-Za-z0-9.-]+"
               r"\.[A-Za-z]{2,5}",text)

# 1. r"[A-Za-z0-9_%+-.]+"

# This expression looks for a continuous sequence of characters consist 
#  all capital alphabets defined by A-Z,
#  lowercase alphabets a-z, all digits 0-9,
#  and special characters such as _%+-. . 
# The '+' is used to append the second regex to the first.

# 2. r"@[A-Za-z0-9.-]+"

# This expression looks for a continuous sequence of characters consist of
#  all capital alphabets defined by A-Z, 
# lowercase alphabets a-z, all digits 0-9, and 
# special characters such as ._. 
# The '+' is used to append the second regex to the first.

# 3. r"\.[A-Za-z]{2,5}"

# This expression looks for a continuous sequence of characters consist of
#  all capital alphabets defined by A-Z, 
# lowercase alphabets a-z such that the size of this continuous sequence is between 2-5 both inclusive.
# printing all the emails found
print(reg)