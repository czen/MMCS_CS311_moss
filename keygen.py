from os import chmod, mkdir, path
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend


def make_key(login):
    if path.exists("./keys/{}/private.key".format(login)):
        return
    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )
    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption())
    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    mkdir("./keys/{}".format(login))
    with open("./keys/{}/private.key".format(login), 'wb') as content_file:
        chmod("./keys/{}/private.key".format(login), 0o600)
        content_file.write(private_key)
    with open("./keys/{}/public.key".format(login), 'wb') as content_file:
        content_file.write(public_key)


if __name__=="__main__":
    make_key('ev')