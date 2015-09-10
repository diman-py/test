from pip._vendor.requests.packages.urllib3.connectionpool import xrange

a = [i for i in xrange(50, 100, 5) ]

a = str(a)

print(a)

f=open('text.txt', 'a')
f.write(a)
f.close()