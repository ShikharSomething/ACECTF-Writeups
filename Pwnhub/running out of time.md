`Running Out of Time`

Just write a script that `XOR` again the value in `p3xr9q_t1zz` function

```c
int p3xr9q_t1zz()
{
  _BYTE v1[27]; // [rsp+20h] [rbp-20h]
  char n42; // [rsp+3Bh] [rbp-5h]
  unsigned int i; // [rsp+3Ch] [rbp-4h]

  v1[0] = '\x1D';
  v1[1] = '\x1B';
  v1[2] = 'G';
  v1[3] = '\x19';
  v1[4] = 'u';
  v1[5] = '\x1F';
  v1[6] = '\x1D';
  v1[7] = '\x1A';
  v1[8] = 'Z';
  v1[9] = 'Z';
  v1[10] = '\x19';
  v1[11] = 'N';
  n42 = '*';
  printf("Success! Here is your output: ");
  for ( i = 0; i <= 0xB; ++i )
    putchar(n42 ^ v1[i]);
  return putchar(10);
}
```

Script: 
```py
#!/usr/bin/env python3

def main():

    bytes_v1 = [0x1D, 0x1B, ord('G'), 0x19, ord('u'), 0x1F, 0x1D, 0x1A, ord('Z'), ord('Z'), 0x19, ord('N')]
    key = ord('*')  

    flag = ''.join(chr(b ^ key) for b in bytes_v1)
    print("Success! Here is your output:", flag)

if __name__ == "__main__":
    main()```