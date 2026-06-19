def transaction_id_generator():
    transaction_id = 1

    while True:
        yield f"TXN-{transaction_id}"
        transaction_id += 1

    
txn_gen = transaction_id_generator()

print("First Transaction", next(txn_gen))
print("Second Transaction", next(txn_gen))
print("Third Transaction", next(txn_gen))


print(transaction_id_generator())