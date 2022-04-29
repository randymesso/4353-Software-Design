from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def hashPassword(password):
  digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
  digest.update(str.encode(password))
  return digest.finalize()

#get hashed_password from user model
def verifyPassword(input_password,hashed_password):
  digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
  digest.update(str.encode(input_password))
  return digest.finalize() == hashed_password

print(verifyPassword('password',hashPassword('password')))