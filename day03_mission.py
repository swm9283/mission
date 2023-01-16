#mission 1
#5.4
salutation = "Hello"
name = "Seojin"
product = "espresso machine"
verbed = "is"
room = "kitchen"
animals = "흰코(cats)"
amount = "100$"
percent = "10%"
spokeman = "woomin"
job_title = "your boyfriend"
letter = """    Dear {0} {1},
    Tkank you for your letter. We are sorry that our {2} {3} in your {4}. Please note that it should never be used in
a {4}, especially near any {5}.

    send your receipt and {6} for shipping and handling. we will send you another {2} that, in out tests, is {7}% less
likely to have{3}.
    Thank you for your support.
    Sincerely,
    {8}
    {9}"""
print(letter.format(salutation,name,product,verbed,room,animals,amount,percent,spokeman,job_title))




