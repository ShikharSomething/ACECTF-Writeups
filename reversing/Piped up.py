#!/usr/bin/env python
from pwn import xor

expected = bytearray(39)
expected[0:2] = b'l,'
expected[2] = (-32) & 0xff ;
expected[3] = (-17) & 0xff ;
expected[4] = (-115) & 0xff ;
expected[5] = 96;
expected[6] = (-36) & 0xff ;
expected[7] = 117;
expected[8] = 13;
expected[9] = (-1) & 0xff ;
expected[10] = (-42) & 0xff ;
expected[11] = 89;
expected[12] = (-12) & 0xff ;
expected[13] = 93;
expected[14] = (-34) & 0xff ;
expected[15] = (-101) & 0xff ;
expected[16] = (-29) & 0xff ;
expected[17] = (-41) & 0xff ;
expected[18] = 82;
expected[19] = (-103) & 0xff ;
expected[20] = 90;
expected[21] = 124;
expected[22] = (-93) & 0xff ;
expected[23] = (-55) & 0xff ;
expected[24] = 78;
expected[25] = 27;
expected[26] = 69;
expected[27] = (-27) & 0xff ;
expected[28] = (-64) & 0xff ;
expected[29] = 41;
expected[30] = (-102) & 0xff ;
expected[31:35] = p32(39)
print(f'{expected = }')

out2 = bytearray(39)
out2[:2] = b"{."
out2[2] = (-15) & 0xff ;
out2[3] = (-21) & 0xff ;
out2[4] = (-117) & 0xff ;
out2[5] = 118;
out2[6] = (-25) & 0xff ;
out2[7] = 104;
out2[8] = 119;
out2[9] = (-93) & 0xff ;
out2[10] = (-17) & 0xff ;
out2[11] = 82;
out2[12] = (-10) & 0xff ;
out2[13] = 60;
out2[14] = (-38) & 0xff ;
out2[15] = (-86) & 0xff ;
out2[16] = (-10) & 0xff ;
out2[17] = (-89) & 0xff ;
out2[18] = 67;
out2[19] = (-21) & 0xff ;
out2[20] = 33;
out2[21] = 36;
out2[22] = (-61) & 0xff ;
out2[23] = (-100) & 0xff ;
out2[24] = 125;
out2[25] = 8;
out2[26] = 51;
out2[27] = (-73) & 0xff ;
out2[28] = (-9) & 0xff ;
out2[29] = 44;
out2[30] = (-76) & 0xff ;
print(f'{out2 = }')

step4 = xor(expected, out2)
print(f'{step4 = }')

step7 = bytearray(step4)
for i in range(len(step4) - 1, 0, -1):
    # print(f'{i = }')
    step7[i] = step7[i] ^ step4[i - 1]
print(f'{step7 = }')

step3 = xor(0x56, step7)
print(f'{step3 = }')
