# Filename: q4p3.py
# Author: William Lohmann, 000762544
# Course: ITSC203
# Details:

import pefile 


# First 4: magic number
# 5th byte: 1 for 32bit 2 for 64bit
# 6th: 1 or 2 for little or big endianess
# 7th: set to 1 for current ELF
# 8th: set to 0 - 18 based on the ABI
# 17&18: object file type, 0x00 to 0xFFFF, 0-4 are file type, rest are saved for OS 
# 19 & 20: ISA

fpath = "investigate.out"

with open(fpath, 'rb') as elfFile:
	elfHeader = elfFile.read(64)
	
	
#################### Bit size examination ####################


if elfHeader[4] == 1:
	print("This is a 32bit file")
	
elif elfHeader[4] == 2:
	print("This is a 64bit file")
	

####################### ABI examination #######################


ABI_dict = {'0':'System V', '1':'HP-UX', '2':'NetBSD', '3':'Linux', '4':'GNU', '6':'solaris', '7':'AIX', '8':'irix', '9':'FreeBSD', '10':'True64', '11':'Novell', '12':'OpenBSD', '13':'OpenVMS', '14':'NonStop Kernel', '15':'AROS', '16':'FenixOS', '17':'Nuxi CloudABI', '18':'Stratus OpenVOS'} # From wiki page for ELF files

OS_ABI = str(elfHeader[7])

for abi in ABI_dict:
	if abi == OS_ABI:
		print("\nTarget OS ABI:",ABI_dict[abi])
		


####################### File type check #######################


fType = elfHeader[16]

if fType == 1:
	print("\nThis is a relocatable file")

elif fType == 2:
	print("\nThis is an executable file")
	
elif fType == 3:
	print("\nThis is a shared object file")
	
	

########################## ISA Check ##########################

ISA_dict = {3:'x86', 7:'Intel 80860', 19:'Intel 80960', 50:'IA-64', 62:'AMD x86-64', 183:'Arm 64', 243:'RISC-V'} # Partial selection from the ELF wiki based on guesstimations for target ISA

ISA = int(elfHeader[18])

for isa in ISA_dict:
	if isa == ISA:
		print("\nTarget ISA:",ISA_dict[isa])
	



