h, z, l = map(int, input().split())
if h > z and h > l and z < l:
    meio = 'luisinho'
elif h > z and h > l and z > l:
    meio = 'zezinho'
elif z > h and z > l and h > l:
    meio = 'huguinho'
elif z > h and z > l and l > h:
    meio = 'luisinho'
elif l > h and l > z and h > z:
    meio = 'huguinho'
elif l > h and l > z and z > h:
    meio = 'zezinho'
print(meio)