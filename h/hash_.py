import hashlib

hash_100 = hashlib.sha1("Password".encode("utf-8")).hexdigest()
for i in range(1, 100):
    hash_100 = hashlib.sha1(hash_100.encode("utf-8")).hexdigest()

hash_99 = hashlib.sha1("Password".encode("utf-8")).hexdigest()
for i in range(1, 99):
    hash_99 = hashlib.sha1(hash_99.encode("utf-8")).hexdigest()

print("hash 99:", hash_99)
print("hash(hash_99):", hashlib.sha1(hash_99.encode("utf-8")).hexdigest())
print("hash_100:", hash_100)
