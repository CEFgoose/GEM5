import re

findFirstName=re.compile('(\s*\"user_.*?\"\s*\)).*?')
findUsername=re.compile('(\s*\"user:.*?\"\s*\)).*?')

FINDUSERNAME = re.compile('(?:|)USERNAME(?:|\W)')
FINDUSERID = re.compile('(?:|)USERID(?:|\W)')
FINDUSERNODESIZE = re.compile('(?:|)USERNODESIZE(?:|\W)')
FINDUSERNODECOLOR = re.compile('(?:|)USERNODECOLOR(?:|\W)')
FINDUSERNODESHAPE = re.compile('(?:|)USERNODESHAPE(?:|\W)')
FINDUSERWAYWIDTH = re.compile('(?:|)USERWAYWIDTH(?:|\W)')
FINDUSERWAYCOLOR = re.compile('(?:|)USERWAYCOLOR(?:|\W)')

FINDNOTUPNODESIZE = re.compile('(?:|)NOTUPNODESIZE(?:|\W)')
FINDNOTUPNODECOLOR = re.compile('(?:|)NOTUPNODECOLOR(?:|\W)')

FINDNOTUPNODESHAPE = re.compile('(?:|)NOTUPNODESHAPE(?:|\W)')
FINDNOTUPWAYCOLOR = re.compile('(?:|)NOTUPWAYCOLOR(?:|\W)')
FINDNOTUPWAYWIDTH = re.compile('(?:|)NOTUPWAYWIDTH(?:|\W)')
FINDTIMESEARCH = re.compile('(?:|)SEARCHTIME(?:|\W)')
FINDTITLE = re.compile('(?:|)TITLE(?:|\W)')

