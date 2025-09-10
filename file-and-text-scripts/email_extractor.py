#Email Extractor , Script 13. From a given text, extract words with @.
# username@domain.extension
text="hello, this is vinod. my email is vinod@fun.com  " \
"and my friends email is friend@fun.com , " \
"my brother also has email vinod_bro@family.technology" \
" one more vinod_bro@family.technology"
# importing regex module.
import re
reg=re.findall(r"[A-Za-z0-9_%+-.]+" 
               r"@[A-Za-z0-9.-]+"
               r"\.[A-Za-z]{2,}",text)

# 1. r"[A-Za-z0-9_%+-.]+"
# This matches the username part before the @.

# 2. r"@[A-Za-z0-9.-]+"
# @ Literally matches the @ symbol.
# This matches the domain name part.
# 3. r"\.[A-Za-z]{2,}"
#This matches the top-level domain like .com, .org, .net, .info. 

# Ignore duplicates (if the same email repeats in text)
email=list(set(reg))
print(email)


# Extract from files instead of inline text
# with open("emails.txt", "r") as f:
#     content = f.read()
# emails = re.findall(r"[A-Za-z0-9_%+-.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", content)
# print(emails)
