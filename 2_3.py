# print("one", "two", "three", sep=", ")

# print("Hello", end=" ")
# print("World!")
# print("a\tb\tc") #\t is a special character to add a tab between index

# print("a\tb\nc\td\ne\tf")

# print("0123456789012345678901234567890")

# str1 = "there is a {0}% probability the the stock market will crash tomorrow but a {1}% chance for the next day."
# print(str1.format(10, 50))

# print("01234567890123456789")
# print("{0:^5s}{1:<20s}{2:>3s}".format("Rank","Player","HR"))
# print("{0:^5n}{1:<20s}{2:>3n}".format(1,"Barry Bonds",762))
# print("{0:^5n}{1:<20s}{2:>3n}".format(2,"Hank Aaron",755))
# print("{0:^5n}{1:<20s}{2:>3n}".format(3,"Babe Ruth",714))

print("The area of {0:s} is {1:,d} square miles.".format("Texas",268820))
str2 = "Of the total US population, {0:.2%} resides in {1:s}."
print(str2.format(2644800/30900000,"Texas"))