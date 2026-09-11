"""Signs a ball serial with the Silph key."""
import hashlib
import hmac


def load_key():
    import os
    return os.environ["SILPH_MB_KEY"]


def sign(serial):
    return hmac.new(load_key().encode(), serial.encode(), hashlib.sha256).hexdigest()
