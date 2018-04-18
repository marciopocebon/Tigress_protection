#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5472 = ref_278 # MOV operation
ref_5514 = ref_5472 # MOV operation
ref_5522 = (ref_5514 >> (0x3 & 0x3F)) # SHR operation
ref_5529 = ref_5522 # MOV operation
ref_5997 = ref_278 # MOV operation
ref_6029 = ref_5997 # MOV operation
ref_6043 = ((ref_6029 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_6080 = ref_5529 # MOV operation
ref_6092 = ref_6043 # MOV operation
ref_6094 = (ref_6092 | ref_6080) # OR operation
ref_6131 = ref_6094 # MOV operation
ref_6145 = ((ref_6131 - 0x3FEFFF7F) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_6153 = ref_6145 # MOV operation
ref_6187 = ref_6153 # MOV operation
ref_6189 = ((ref_6187 >> 56) & 0xFF) # Byte reference - MOV operation
ref_6190 = ((ref_6187 >> 48) & 0xFF) # Byte reference - MOV operation
ref_6191 = ((ref_6187 >> 40) & 0xFF) # Byte reference - MOV operation
ref_6192 = ((ref_6187 >> 32) & 0xFF) # Byte reference - MOV operation
ref_6193 = ((ref_6187 >> 24) & 0xFF) # Byte reference - MOV operation
ref_6194 = ((ref_6187 >> 16) & 0xFF) # Byte reference - MOV operation
ref_6195 = ((ref_6187 >> 8) & 0xFF) # Byte reference - MOV operation
ref_6196 = (ref_6187 & 0xFF) # Byte reference - MOV operation
ref_6840 = ref_278 # MOV operation
ref_7070 = ref_6187 # MOV operation
ref_7096 = ref_6840 # MOV operation
ref_7100 = ref_7070 # MOV operation
ref_7102 = (ref_7100 | ref_7096) # OR operation
ref_7139 = ref_7102 # MOV operation
ref_7153 = ((ref_7139 - 0x11E59B96) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7161 = ref_7153 # MOV operation
ref_7195 = ref_7161 # MOV operation
ref_7197 = ((ref_7195 >> 56) & 0xFF) # Byte reference - MOV operation
ref_7198 = ((ref_7195 >> 48) & 0xFF) # Byte reference - MOV operation
ref_7199 = ((ref_7195 >> 40) & 0xFF) # Byte reference - MOV operation
ref_7200 = ((ref_7195 >> 32) & 0xFF) # Byte reference - MOV operation
ref_7201 = ((ref_7195 >> 24) & 0xFF) # Byte reference - MOV operation
ref_7202 = ((ref_7195 >> 16) & 0xFF) # Byte reference - MOV operation
ref_7203 = ((ref_7195 >> 8) & 0xFF) # Byte reference - MOV operation
ref_7204 = (ref_7195 & 0xFF) # Byte reference - MOV operation
ref_7893 = ref_278 # MOV operation
ref_8123 = ref_6187 # MOV operation
ref_8149 = ref_7893 # MOV operation
ref_8153 = ref_8123 # MOV operation
ref_8155 = (((sx(0x40, ref_8153) * sx(0x40, ref_8149)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8447 = ref_7195 # MOV operation
ref_8471 = ref_8447 # MOV operation
ref_8479 = ((ref_8471 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_8486 = ref_8479 # MOV operation
ref_8512 = ref_8155 # MOV operation
ref_8516 = ref_8486 # MOV operation
ref_8518 = (((sx(0x40, ref_8516) * sx(0x40, ref_8512)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_8554 = ref_8518 # MOV operation
ref_9383 = ref_278 # MOV operation
ref_9415 = ref_9383 # MOV operation
ref_9429 = ((ref_9415 - 0x2000000007A4C37E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9437 = ref_9429 # MOV operation
ref_9471 = ref_9437 # MOV operation
ref_10572 = ((((ref_6189) << 8 | ref_6190) << 8 | ref_6191) << 8 | ref_6192) # MOV operation
ref_10646 = (ref_10572 & 0xFFFFFFFF) # MOV operation
ref_11270 = ((((ref_6193) << 8 | ref_6194) << 8 | ref_6195) << 8 | ref_6196) # MOV operation
ref_11780 = (ref_11270 & 0xFFFFFFFF) # MOV operation
ref_11782 = (((ref_11780 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_11783 = (((ref_11780 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_11784 = (((ref_11780 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_11785 = ((ref_11780 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_11945 = (ref_10646 & 0xFFFFFFFF) # MOV operation
ref_12455 = (ref_11945 & 0xFFFFFFFF) # MOV operation
ref_12457 = (((ref_12455 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_12458 = (((ref_12455 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_12459 = (((ref_12455 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_12460 = ((ref_12455 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_13166 = ((((((((ref_11782) << 8 | ref_11783) << 8 | ref_11784) << 8 | ref_11785) << 8 | ref_12457) << 8 | ref_12458) << 8 | ref_12459) << 8 | ref_12460) # MOV operation
ref_13580 = ref_8554 # MOV operation
ref_13854 = ref_8554 # MOV operation
ref_13886 = ref_13580 # MOV operation
ref_13898 = ref_13854 # MOV operation
ref_13900 = ((ref_13898 + ref_13886) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_13956 = ref_13900 # MOV operation
ref_13970 = (0x3F & ref_13956) # AND operation
ref_13999 = ref_13970 # MOV operation
ref_14007 = ((ref_13999 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14014 = ref_14007 # MOV operation
ref_14040 = ref_13166 # MOV operation
ref_14044 = ref_14014 # MOV operation
ref_14046 = (ref_14044 | ref_14040) # OR operation
ref_14085 = ref_14046 # MOV operation
ref_15403 = ((((ref_7197) << 8 | ref_7198) << 8 | ref_7199) << 8 | ref_7200) # MOV operation
ref_15477 = (ref_15403 & 0xFFFFFFFF) # MOV operation
ref_16101 = ((((ref_7201) << 8 | ref_7202) << 8 | ref_7203) << 8 | ref_7204) # MOV operation
ref_16611 = (ref_16101 & 0xFFFFFFFF) # MOV operation
ref_16613 = (((ref_16611 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_16614 = (((ref_16611 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_16615 = (((ref_16611 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_16616 = ((ref_16611 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_16776 = (ref_15477 & 0xFFFFFFFF) # MOV operation
ref_17286 = (ref_16776 & 0xFFFFFFFF) # MOV operation
ref_17288 = (((ref_17286 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_17289 = (((ref_17286 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_17290 = (((ref_17286 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_17291 = ((ref_17286 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_17997 = ((((((((ref_16613) << 8 | ref_16614) << 8 | ref_16615) << 8 | ref_16616) << 8 | ref_17288) << 8 | ref_17289) << 8 | ref_17290) << 8 | ref_17291) # MOV operation
ref_18411 = ref_9471 # MOV operation
ref_18685 = ref_8554 # MOV operation
ref_18717 = ref_18411 # MOV operation
ref_18729 = ref_18685 # MOV operation
ref_18731 = ((ref_18729 + ref_18717) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_18787 = ref_18731 # MOV operation
ref_18801 = (0x3F & ref_18787) # AND operation
ref_18830 = ref_18801 # MOV operation
ref_18838 = ((ref_18830 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18845 = ref_18838 # MOV operation
ref_18871 = ref_17997 # MOV operation
ref_18875 = ref_18845 # MOV operation
ref_18877 = (ref_18875 | ref_18871) # OR operation
ref_18916 = ref_18877 # MOV operation
ref_18918 = ((ref_18916 >> 56) & 0xFF) # Byte reference - MOV operation
ref_18919 = ((ref_18916 >> 48) & 0xFF) # Byte reference - MOV operation
ref_18920 = ((ref_18916 >> 40) & 0xFF) # Byte reference - MOV operation
ref_18921 = ((ref_18916 >> 32) & 0xFF) # Byte reference - MOV operation
ref_18922 = ((ref_18916 >> 24) & 0xFF) # Byte reference - MOV operation
ref_18923 = ((ref_18916 >> 16) & 0xFF) # Byte reference - MOV operation
ref_18924 = ((ref_18916 >> 8) & 0xFF) # Byte reference - MOV operation
ref_18925 = (ref_18916 & 0xFF) # Byte reference - MOV operation
ref_20373 = ref_18920 # MOVZX operation
ref_20443 = (ref_20373 & 0xFF) # MOVZX operation
ref_20889 = ref_18924 # MOVZX operation
ref_21464 = (ref_20889 & 0xFF) # MOVZX operation
ref_21466 = (ref_21464 & 0xFF) # Byte reference - MOV operation
ref_21510 = (ref_20443 & 0xFF) # MOVZX operation
ref_21954 = (ref_21510 & 0xFF) # MOVZX operation
ref_21956 = (ref_21954 & 0xFF) # Byte reference - MOV operation
ref_22740 = ref_8554 # MOV operation
ref_23014 = ref_9471 # MOV operation
ref_23030 = ref_22740 # MOV operation
ref_23042 = ref_23014 # MOV operation
ref_23044 = (ref_23042 & ref_23030) # AND operation
ref_23083 = ref_23044 # MOV operation
ref_23097 = (0xF & ref_23083) # AND operation
ref_23136 = ref_23097 # MOV operation
ref_23150 = (0x1 | ref_23136) # OR operation
ref_23532 = ref_14085 # MOV operation
ref_23806 = ((((((((ref_18918) << 8 | ref_18919) << 8 | ref_21466) << 8 | ref_18921) << 8 | ref_18922) << 8 | ref_18923) << 8 | ref_21956) << 8 | ref_18925) # MOV operation
ref_23822 = ref_23532 # MOV operation
ref_23834 = ref_23806 # MOV operation
ref_23836 = ((ref_23834 + ref_23822) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_23860 = ref_23836 # MOV operation
ref_23872 = ref_23150 # MOV operation
ref_23874 = ((ref_23860 << ((ref_23872 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_24109 = ref_14085 # MOV operation
ref_24383 = ((((((((ref_18918) << 8 | ref_18919) << 8 | ref_21466) << 8 | ref_18921) << 8 | ref_18922) << 8 | ref_18923) << 8 | ref_21956) << 8 | ref_18925) # MOV operation
ref_24399 = ref_24109 # MOV operation
ref_24411 = ref_24383 # MOV operation
ref_24413 = ((ref_24411 + ref_24399) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_24768 = ref_8554 # MOV operation
ref_25042 = ref_9471 # MOV operation
ref_25074 = ref_24768 # MOV operation
ref_25086 = ref_25042 # MOV operation
ref_25088 = (ref_25086 & ref_25074) # AND operation
ref_25143 = ref_25088 # MOV operation
ref_25157 = (0xF & ref_25143) # AND operation
ref_25212 = ref_25157 # MOV operation
ref_25226 = (0x1 | ref_25212) # OR operation
ref_25293 = ref_25226 # MOV operation
ref_25295 = ((0x40 - ref_25293) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_25303 = ref_25295 # MOV operation
ref_25319 = ref_24413 # MOV operation
ref_25331 = ref_25303 # MOV operation
ref_25333 = (ref_25319 >> ((ref_25331 & 0xFF) & 0x3F)) # SHR operation
ref_25364 = ref_23874 # MOV operation
ref_25368 = ref_25333 # MOV operation
ref_25370 = (ref_25368 | ref_25364) # OR operation
ref_25409 = ref_25370 # MOV operation
ref_25688 = ref_25409 # MOV operation
ref_25690 = ref_25688 # MOV operation

print ref_25690 & 0xffffffffffffffff