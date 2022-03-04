import re

findFirstName=re.compile('(\s*\"user_.*?\"\s*\)).*?')
findUsername=re.compile('(\s*\"user:.*?\"\s*\)).*?')