def transaction(message):
    """This is the function for adding transaction history to the file with .log extension"""
    with open('transaction.log','a') as f:
        f.write(message+'\n')

# help(transaction)