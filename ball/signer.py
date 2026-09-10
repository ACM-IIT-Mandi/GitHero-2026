"""Signs a ball serial with the Silph key."""
import hashlib
import hmac


def load_key():
    return open("config/signing.ini").read().split("key = ")[1].split()[0]


def sign(serial):
    return hmac.new(load_key().encode(), serial.encode(), hashlib.sha256).hexdigest()
