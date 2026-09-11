#!/bin/sh
# Usage: tools/sign.sh <ball-serial>
KEY="MBK-4f9a2c7e81d35b60a7c94e12f8d06b3a"
printf '%s' "$1" | openssl dgst -sha256 -hmac "$KEY"
