def announce(f):
    def wrapper():
        print("starting the machine ......")
        f()
        print ("Shutting down the machine.")
    return wrapper

@announce
def hello():
    print("==== Mouve ====!")

hello()