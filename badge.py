"""GitHero badge generator.
Usage: python badge.py <your-github-username> <answer>
Prints an 8-character badge. Paste it in your proof.md.
"""
import hashlib
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python badge.py <your-github-username> <answer>")

username, answer = sys.argv[1], sys.argv[2]
print(hashlib.sha256(f"{username}:{answer}".encode()).hexdigest()[:8])
