#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

H, W = map(int, input().split())
h, w = map(int, input().split())

math_count = H * W
delete_math_count = (h * W) + (w * (H - h))

print(math_count - delete_math_count)
