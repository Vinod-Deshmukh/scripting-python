#Email Extractor , Script 13. From a given text, extract words with @.
text="hello, this is vinod. my email is vinod@fun.com  " \
"and my friends email is friend@fun.com , " \
"my brother also has email vinod_bro@family.co.uk"
# importing regex module.
import re
reg=re.findall(r"[A-Za-z0-9_%+-.]+" 
               r"@[A-Za-z0-9.-]+"
               r"\.[A-Za-z]{2,5}",text)

reg2 = re.findall(r"[A-Za-z0-9_%+-.]+"
                 r"@[A-Za-z0-9.-]+"
                 r"\.[A-Za-z]{2,5}",text)

# printing all the emails found
print(reg)