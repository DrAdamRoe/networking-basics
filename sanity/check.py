import sys

if sys.version_info < (3,0):
    print("\ninsane!\n")
    print("This requires Python 3.x. You are using version %i.%i \n" % (sys.version_info.major,sys.version_info.minor ))
    sys.exit(1)

print("You are sane. Whew.")
