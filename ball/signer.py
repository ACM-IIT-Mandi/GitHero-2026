"""Signs a ball serial with the Silph key."""
import hashlib
import hmac


def load_key():
    return open("keys/masterball.key").read().strip()


def sign(serial):
    return hmac.new(load_key().encode(), serial.encode(), hashlib.sha256).hexdigest()
