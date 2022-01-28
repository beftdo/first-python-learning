'''
바이트는 바이트의 튜플처럼 불변(immutable)한다.
바이트 배열(bytearray)은 바이트의 리스트처럼 가변(mutable)이다.
'''

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes) 
#바이트 값은 b로 시작 그다음 인용 부호가 따라옴. 
#인용 부호 안에는 \x01 or 아스키 문자 같은 16진수 시퀀스가 옮.
the_byte_array = bytearray(blist)
print(the_byte_array)

'''blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
the_bytes[1] = 127
예외가 발생했습니다. TypeError
'bytes' object does not support item assignment
바이트 변수는 불변
'''

#바이트 배열 변수는 변경 가능
blist = [1, 2, 3, 255]
the_byte_array = bytearray(blist)
print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)

#0부터 255까지 256개의 결과 생성
the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))
#파이썬은 출력할 수 없는 바이트에 대해서는 \xxx를 사용하고, 
#출력할 수 있는 바이트에 대해서는 아스키 코드 값을 사용한다
print(the_bytes)
print("---------------------------------------------------------------------")

'''
struct 모듈 : 이진 데이터를 파이썬 데이터 구조로 바꾸거나
파이썬 데이터 구조를 이진 데이터로 바꿀 수 있다.
'''

import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
# 라인을 유지하는 문자 \
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')
#width : 16~19바이트에서 추출, height : 20~23바이트에서 추출
#>LL은 입력한 바이트 시퀀스를 해석하고, 파이썬의 데이터 형식으로 만들어주는 형식 문자열(fomat string)
#>는 정수가 big-endian 형식으로 저장되었다는 것을 의미
# 각각의 L은 4바이트의 부호 없는 long 정수를 지정

print(data[16:20])
print(data[20:24])
print(struct.unpack('>LL', data[16:24]))