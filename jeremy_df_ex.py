# examples of things you can do with dataframes in pandas


import pandas as pd
import numpy as np
import re


def printDiv(divlen = 20, divchar = "--"):
	if divlen > 0:
		i = 0
		while i < divlen:
			print(divchar, end='')
			i += 1
		print("")


def getListAsString(myList, showType = True):
	thingTypeRaw = str(type(myList))
	thingTypeDeterm = False
	kv = False

	if re.match(".*class 'dict'.*", thingTypeRaw):
		thingTypeDeterm = "recognized as dict"
		kv = True

	if re.match(".*pandas.core.series.Series.*", thingTypeRaw):
		thingTypeDeterm = "recognized as pd.Series"
		kv = True

	if re.match(".*pandas.core.indexes.base.Index*", thingTypeRaw):
		thingTypeDeterm = "recognized as pd.Index"
		kv = False

	if not thingTypeDeterm:
		thingTypeDeterm = "unrecognized: " + thingTypeRaw

	returnString = ""
	if kv:
		for k, v in myList.items():  
			returnString += str(k) +  "->" + str(v) + "  "
	else:
		returnString += myList
	
	if showType:
		returnString += "(" + thingTypeDeterm + ")"

	return returnString


def showRemindersTypes(div=True):
	if div:
		printDiv()
	print("types...")
	X = ["this", "is", "a", "list"]
	for item in X:
		print("  ",item)
	Y = ("i", "am", "a", "tuple") 
	print("X:", X, "type(X):", type(X))
	print("Y:", Y, "type(Y):", type(Y))

	ex_dictionary = {"A" : "90 or higher",
					"B" : "[80-90)",
					"C" : "[70-80)",
					"D" : "[60-70)",
					"F" : "Below 60"}

	for key in ex_dictionary:
		print("  ", key, "->", ex_dictionary[key])

	print("ex_dictionary:", ex_dictionary)
	print("type(ex_dictionary:", type(ex_dictionary))
	print("len(ex_dictionary:", len(ex_dictionary))



def showRemindersNumpy(div = True):
	if div:
		printDiv()
	print("numpy...")
	X = np.random.randint(0, 100, (3,5))
	print("np.random.randint = [min,max), (shape)")
	print("np.random.randint = [min,max), (rows,cols,...)")
	print("X:\n", X)
	print("type(X):", type(X))
	print("len(X):", len(X))
	print("X.shape:", X.shape)
	print("X.shape[0]:", X.shape[0], "rows")
	print("X.shape[1]:", X.shape[1], "cols")

	X = np.random.randint(0, 100, (10, 20))
	print(X)

	print("np.sort(X,axis=0): (each column)\n", np.sort(X,axis=0))
	print("np.sort(X,axis=1): (each row)\n", np.sort(X,axis=1))


def showRemindersSeriesA(div=True):
	if div:
		printDiv()
	print("panas series from lists part A")

	alist = ["eat", 'my', 'shorts']
	aseries = pd.Series(alist)
	print("alist:\n", alist)
	print("aseries:\n", aseries)
	print("type(alist):  ", type(alist))
	print("type(aseries):", type(aseries))

	blist = ["hello", 27,True, 3.9]

	nfl_loc  = ["Green Bay", "San Francisco", "Oakland", "Chicago"]
	nfl_name = ["Packers", "49ers", "Raiders", "Bears"]

	nflSeriesByName = pd.Series(nfl_loc, index=nfl_name)
	nflSeriesByLoc = pd.Series(nfl_name, index=nfl_loc)
	print("nflSeriesByName:\n", nflSeriesByName)
	print("nflSeriesByLoc:\n", nflSeriesByLoc)
	print("nflSeriesByName[\"Packers\"]:", nflSeriesByName["Packers"])
	print("nflSeriesByLoc[\"Chicago\"]:", nflSeriesByLoc["Chicago"])

	print("use integer index or iloc")
	print("  nflSeriesByName.iloc[2]:",nflSeriesByName.iloc[2])  # oakland
	print("  nflSeriesByName[2]:     ",nflSeriesByName[2])  # oakland

	print("use label index or loc")
	print("  nflSeriesByName.loc[\"Packers\"]:",nflSeriesByName.loc["Packers"])  # greenbay
	print("  nflSeriesByName[\"Packers\"]    :",nflSeriesByName["Packers"])  # greenbay
	#print("  nflSeriesByName[2]:     ",nflSeriesByName[2])  # oakland


def showRemindersSeriesB(div=True):
	if div:
		printDiv()

	print("panas series from lists part A")


	oddDictA = {98: "A", 99: "B", 100: "C", 101: "D", 102: "E"}
	oddSeriesA = pd.Series(oddDictA)
	oddDictB = {v: k for k, v in oddDictA.items()}  # reverse dict
	oddSeriesB = pd.Series(oddDictB)

	"""
	loc gets rows (or columns) with particular labels from the index.
	iloc gets rows (or columns) at particular positions in the index (so it only takes integers).
	ix usually tries to behave like loc but falls back to behaving like iloc if a label is not present in the index.
	"""

	printDiv()
	print("oddDictA: ", getListAsString(oddDictA))
	print("  valid ops:")
	print("     oddDictA[99]:       ", oddDictA[99], " # by index label")
	print("  invalid calls include:")
	print("     oddDictA[2]:            # no such label")
	print("     oddDictA[\"99\"]:         # label is an int, not a string")
	print("     (no methods .loc .iloc .ix)")
	print("oddDictB: ", getListAsString(oddDictB))
	print("  valid ops:")
	print("     oddDictB[\"B\"]:      ", oddDictB["B"], "# by index label")
	print("  invalid calls include:")
	print("     oddDictA[2]:            # no such label")
	print("     oddDictA[B]:            # label is a string, not an int")
	print("     (no methods .loc .iloc .ix)")

	printDiv()
	print("oddSeriesA: ", getListAsString(oddSeriesA))
	print("  valid ops:")
	print("     oddSeriesA[99]:      ", oddSeriesA[99], "   # by index label")
	print("     oddSeriesA.loc[99]:  ", oddSeriesA.loc[99], "   # by index label")
	print("     oddSeriesA.iloc[2]:  ", oddSeriesA.iloc[2], "   # by index int")  
	print("     oddSeriesA.ix[99]:   ", oddSeriesA.ix[99],  "   # if lab is present: loc else: iloc")  
	print("  invalid calls include:")
	print("     oddSeriesA.iloc[99]        # no index that high")
	print("     oddSeriesA[\"D\"]            # no such index or label")
	print("     oddSeriesA.loc[\"D\"]        # loc  requires a row or col name")
	print("     oddSeriesA.iloc[\"D\"]       # iloc requires an int")
	print("     oddSeriesA.ix[2]:          # label is present so is liek i.loc")  
	print("     note there is no search by key value")



	print("oddSeriesB: ", getListAsString(oddSeriesB))
	print("  valid ops:")
	print("     oddSeriesB[\"C\"]:      ", oddSeriesB["C"], "   # by index label")
	print("     oddSeriesB.loc[\"C\"]:  ", oddSeriesB.loc["C"], "   # by index label")
	print("     oddSeriesB.iloc[2]:   ", oddSeriesB.iloc[2], "   # by index int")  
	print("     oddSeriesB.ix[\"C\"]:   ", oddSeriesB.ix["C"],  "   # if lab is present: loc else: iloc")  
	print("  invalid calls include:")
	print("     oddSeriesB[99]             # no index that high")
	print("     oddSeriesB.iloc[99]        # no index that high")
	print("     oddSeriesB.loc[3]          # no such index label")
	print("     oddSeriesB.ix[3]           # no such index label")
	print("     note there is no search by key value")








def showRemindersDataFrame(div = True):
	if div:
		printDiv()

	olympicsfilename = 'olympics.csv'

	try:
		df = pd.read_csv(olympicsfilename, index_col=0, skiprows=1)
	except IOError:
		print("sorry, can't find", olympicsfilename, " - exiting")
		exit()


	print("pd.read_csv loads as a dataframe:", type(df))

	print("len(df):", len(df))

	print("df.columns", df.columns)

	print("cleaning up round 1")
	for col in df.columns:
	    if col[:2]=='01':
	        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
	        print("  rename", col, "as", "col:Gold" + col[4:] )
	    if col[:2]=='02':
	        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
	        print("  rename", col, "as", "col:Silver" + col[4:] )
	    if col[:2]=='03':
	        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
	        print("  rename", col, "as", "col:Bronze" + col[4:] )
	    if col[:1]=='№':
	        df.rename(columns={col:'#'+col[1:]}, inplace=True)
	        print("  rename", col, "as", "col:#" + col[1:] )


	print("df.columns", df.columns)

	print("cleaning up round 2")
	for col in df.columns:

		colPrefix = False
		if col[:4] == 'Gold':
			colPrefix = col[:4]
		if col[:6] == 'Silver' : colPrefix = col[:6]			
		if col[:6] == 'Bronze' : colPrefix = col[:6]			
		if col[:5] == 'Total' : colPrefix = col[:5]			

		if colPrefix:
			if col[-2:] == ".1":
				df.rename(columns={col:colPrefix + ".Winter"}, inplace = True)
				print("  rename", col, "as", colPrefix + ".Winter" )
			elif col[-2:] == ".2":
				df.rename(columns={col:colPrefix + ".Total"}, inplace = True)
				print("  rename", col, "as", colPrefix + ".Total" )
			else:
				df.rename(columns={col:colPrefix + ".Summer"}, inplace = True)
				print("  rename", col, "as", colPrefix + ".Summer" )


	"""
		if col[:4] == 'Gold':
			if col[-2:] == ".1":
				df.rename(columns={col:"Gold.Winter"}, inplace = True)
				print("  rename", col, "as", "Gold.Winter" )
			elif col[-2:] == ".2":
				df.rename(columns={col:"Gold.Total"}, inplace = True)
				print("  rename", col, "as", "Gold.Total" )
			else:
				df.rename(columns={col:"Gold.Summer"}, inplace = True)
				print("  rename", col, "as", "Gold.Summer" )
"""

	print("df.columns", df.columns)

	print("type(df):", str(type(df)))
	print("  df is a dataframe")


	print("a pandas DataFrame is (rows of series) by cols of ?? ")
	print("str(type(df.iloc[2]):", str(type(df.iloc[2])))


	print("selecting rows and columns directly...")

#	print("-----one country/row all columns-----")
	print("df.iloc[2]  or df.iloc[2,]                     # one row, all cols")
	#print(df.iloc[2])
	#print(df.iloc[2,])

#	print("-----three consecutive countrys/rows all columns-----")
	print("df.iloc[2:5]  or df.iloc[2:5,]                 #   mult rows, all cols")
	#print(df.iloc[2:5])  
	#print(df.iloc[2:5,])  

	print("df.iloc[2][\"Gold.Summer\"]) or df.iloc[2,][\"Gold.Summer\"])        # single entry at one row and one column")
	print(df.iloc[2]["Gold.Summer"])
	print(df.iloc[2,]["Gold.Summer"])

	print("df.iloc[2][[\"Gold.Summer\", \"Gold.Winer\"]]     # single row and mult columns")
	print(df.iloc[2][["Gold.Summer", "Gold.Winter"]])
	print(df.iloc[2,][["Gold.Summer", "Gold.Winter"]])

	print("df.iloc[2:5][[\"Gold.Summer\", \"Gold.Winer\"]]     # multi rows and mult columns - with or without comma") 
	print(df.iloc[2:5][["Gold.Summer", "Gold.Winter"]])
	#print(df.iloc[2:5,][["Gold.Summer", "Gold.Winter"]])


	print("ex = df.loc[:, [\"Gold.Summer\", \"Gold.Winter\", \"Gold.Total\"] ]    # all rows with these three cols" )
	#print(df.loc[:, ["Gold.Summer", "Gold.Winter", "Gold.Total"] ])
	print("note this is NOT a conditional, just showing...")

	ex = df.loc[:, ["Gold.Summer", "Gold.Winter", "Gold.Total"] ]
	print("str(type(ex)):", str(type(ex)))
	print("  ex is a dataframe")
	print("first ten rows:\n", ex[0:9])



	printDiv()
	print("selecting rows and columns with CONDITIONALS...")
	print("Running: ex = df[df[\"Gold.Winter\"] > 3]")
	ex = df[df["Gold.Winter"] > 3]
	print("  len(df):", len(df))
	print("  len(ex):", len(ex))
	print("Running: ex = df[ (df[\"Gold.Winter\"] > 3) | (df[\"Gold.Summer\"] > 20) ]")
	ex = df[       (df["Gold.Winter"] > 3) | (df["Gold.Summer"] > 20)     ] 
	print("  len(ex):", len(ex))
	#print("ex.iloc[:, [\"Gold.Summer\", \"Gold.Winter\"] ]")


	printDiv()
	print("selecting rows and columns with where... converts to NA")
	dfj = df.copy()
	print("dfj = dfj.copy()")
	dfj = dfj.where(dfj["Gold.Winter"] > 4)
	print("dfj = dfj.where(dfj[\"Gold.Winter\"] > 4)")
	# gives us lots of NaN values...
	print("lots of NaN values...")
	#print(dfj[0:10])
	print("len(dfj):", len(dfj))
	print("dfj = dfj.dropna()")
	dfj = dfj.dropna()
	print("len(dfj):", len(dfj))




	print("ex.iloc[0:6][[\"Gold.Summer\", \"Gold.Winter\"] ]    # some rows some cols")  
	print(ex.iloc[0:6][["Gold.Summer", "Gold.Winter"] ])


	printDiv()
	print("start df.iloc[0]")
	print(df.iloc[0])
	print("end df.iloc[0]")



	print("df[\"Gold.Summer\"].idxmax()     # get the row label where Gold.Summer col has max value")
	ex = df["Gold.Summer"].idxmax()
	print(" ex:",ex)
	print("                               # the last row is \"Totals\" which totals all countries")
	print("                               # need to drop this to get good result")
	print("len(df):", len(df))

	print("df.drop(\"Totals\")")
	df = df.drop('Totals')  # otherwise idxmax returns "Totals"...  why??
	print("len(df):", len(df))




	print(str(df["Gold.Summer"].idxmax()))  # find 
	print("    this is correct, row label has funny name until we re-index")


	print("add some fields")
	#df["funnyCode"] = 37      # new field, every row value set to this
	

	print("df.index = the label of the rows")
	print("df.index:", getListAsString(df.index))  # don't know how to iterate through index



	countryTokens = df.index.str.split('\s\(') # split the index by '('
	print("type(countryTokens):", type(countryTokens))
	print("countryTokens.str[0]:", countryTokens.str[0])
	print("countryTokens.str[1]:", countryTokens.str[1])

	df.index = countryTokens.str[0] 		# the [0] element is the country name (new index) 
	df['ID'] = countryTokens.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)




	print(df.columns)



	print(df.columns)

	print(df.head())


	print("Which country has won the most gold medals in summer games?")
	country = df["Gold.Summer"].idxmax()
	# get the index of the row with the maxvalue
	#print("country:", country, "  countryEX:", countryEX)
	print("  df[\"Gold.Summer\"].idxmax():          # returns just the id")
	print( df["Gold.Summer"].idxmax())

	print("  df.ix[df[\"Gold.Summer\"].idxmax()]:    # returns the row")
	#print( df.ix[df["Gold.Summer"].idxmax()])


	print("Which country had the biggest difference between their summer and winter gold medal counts?")
	print("indexVal = (df[\"Gold.Summer\"] - df[\"Gold.Winter\"]).idxmax()")
	indexVal = (df["Gold.Summer"] - df["Gold.Winter"]).idxmax()
	print("indexVal:", indexVal)


	print("Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?  Only include countries that have won at least 1 gold in both summer and winter.")
	dfj = df.copy()

    # only include countries that have won at least one summer gold
	dfj = dfj.where(dfj["Gold.Summer"] > 0)
	dfj = dfj.dropna()
	dfj = dfj.where(dfj["Gold.Winter"] > 0)
	dfj = dfj.dropna()
	print("num countries with at least one summer gold and one winter gold: len(dfj):", len(dfj))
	dfj['gdif'] = dfj["Gold.Summer"] - dfj["Gold.Winter"]       # create a gold summer - gold winter col
	dfj['gratio'] = dfj['gdif'] / dfj["Gold.Total"]
	country = dfj["gratio"].idxmax()
	print(country)

	dfj = df.copy()
	dfj['Points'] = dfj["Gold.Total"] * 3 + dfj["Silver.Total"] * 2 + dfj["Bronze.Total"]

	returnSeries = dfj['Points']

	print("Points:", returnSeries)





showRemindersTypes()
showRemindersNumpy()
showRemindersSeriesA()
showRemindersSeriesB()
showRemindersDataFrame()
#showQADataFrame()
printDiv()

"""
		if col[:4] == 'Gold':
			print("col[:2]", col[:2])
			print("col[2:]", col[2:])
			print("col[-2:]", col[-2:])
"""