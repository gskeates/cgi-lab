#!/usr/bin/env python3

import json
import os

# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

print("Content-Type: text/plain")
print()
print(os.environ['HTTP_USER_AGENT'])
