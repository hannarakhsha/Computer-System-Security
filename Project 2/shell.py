#!/usr/bin/env python
from capstone import *
shellcode = ""
shellcode += "\xebckle\x0e\x5f\x48\x31\xc0\x48\x89\xc6"
shellcode += "\x48\x89\xc2\xb0\x3b\x0f\x05\x48\x31"
shellcode += "\xc0\x48\x89\xc7\xb0\x69\x0f\x05\xe8"
shellcode += "\xe3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68"
md = Cs(CS_ARCH_X86, CS_MODE_32)
for i in md.disasm(shellcode, 0x00):
print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
