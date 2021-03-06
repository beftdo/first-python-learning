#윤년 : isleap 함수는 윤년이면 True 반환 평년이면 False 반환
import calendar
print(calendar.isleap(1900))
print(calendar.isleap(1996))
print(calendar.isleap(1999))
print(calendar.isleap(2000))
print(calendar.isleap(2002))
print(calendar.isleap(2004))

print("---------------------------------------------------------------------")
#datetime 모듈 : 표준 datetime 모듈은 날짜와 시간을 처리
#date : 년, 월, 윌 / time : 시, 분, 초, 마이크로초, 
#datetime : 날짜, 시간/ timedelta : 날짜 및 시간 간격

from datetime import date
halloween = date(2019, 10, 31)
print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)

print(halloween.isoformat())

from datetime import date
now = date.today()
print(now)

from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
print(now + 17*one_day)
yesterday = now - one_day
print(yesterday)

'''날짜의 범위는 date.min(year=1, month=1, day=1) 부터 
date.max(year=9999, month=12, day=31)까지'''
print("---------------------------------------------------------------------")

from datetime import time
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond) #인수를 입력하지 않으면 time 객체의 초기 인수는 0으로 간주

from datetime import datetime
some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
print(some_day)
print(some_day.isoformat()) #isoformat의 중간의 t는 날짜와 시간을 구분함

from datetime import datetime
now = datetime.now() #datetime 객체에서도 now() 메서드로 현재 날짜 시간으 얻을 수 있음.
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

#combine()으로 date 객체와 time 객체를 datetime 객체로 병합할 수 있음.
from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)
print(noon_today.date())
print(noon_today.time())
print("---------------------------------------------------------------------")

'''
time 모듈
datetime 모듈의 time 객체와 / 별도의 time 모듈이 헷갈림. / time 모듈에는 time()는 함수가 존재.

유닉스 시간(절대시간)은 1970년 1월 1일 자정 이후의 시간의 초를 사용 = 에폭(epoch)
time 모듈의 time() 함수는 현재 시간을 에폭 값으로 반환
'''

import time
now = time.time()
print(now)
print(time.ctime(now)) #ctime() 함수를 사용하여 에폭 값을 문자열로 변환
#에폭 값은 자바스크립트와 같은 다른 시스템에서 날짜와 시간을 교환하기 위한 유용한 최소 공통분모

print(time.localtime(now)) #localtime() 메서드는 시간을 시스템의 표준 시간대로 제공
print(time.gmtime(now)) #gmtime() 메서드는 시간을 UTC로 제공
#tm_wday 요일 : 0(월) ~ 6(일)
#tm_yday 년일자 : 1 ~ 366
#tm_isdst 일광 시간 절약제 : 0=아니오, 1=예, -1=모름

import time
now = time.localtime()
print(now)
print(now[0])
print(list(now[x] for x in range(9)))

tm = time.localtime()
print(time.mktime(tm)) 
#mktime() 메서드는 sturct_time 객체를 에폭 초로 변환

import time
now = time.time()
print(time.ctime(now)) #ctime() 함수는 에폭 시간을 문자열로 변환

#strftime()을 사용하여 날짜와 시간을 문자열로 변환할 수 있다.
#문자열의 출력 포맷을 지정
# %Y:년 / %m:월 / %B:월 이름 / %b:월 축약 이름 / %d:월의 일자
# %A:요일 이름 / %a:요일 축약 이름 / %H 24시간 / %I 12시간
# %p:오전/오후 / %M:분 / %S:초

#time 모듈에서 제공하는 strftime()함수
import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
#먼저 포멧 문자열 fmt 정의
t = time.localtime()
print(t)
print(time.strftime(fmt, t))

#date 객체의 strftime 메서드 사용
from datetime import date
some_day = date(2019, 7, 4)
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
print(some_day.strftime(fmt)) 
#날짜 부분만 작동, 시간은 기본값으로 자정으로 지정

#time 객체의 strftime 메서드 사용
from datetime import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
some_time = time(10, 35)
print(some_time.strftime(fmt))

import time
fmt = "%Y-%m-%d"
print(time.strptime("2019-01-29", fmt))

import time
fmt = "%Y %m %d"
print(time.strptime("2019 01 29", fmt))

'''
다른 월, 일의 이름을 출력하려면 setlocale()을 사용하여 국제화 설정인 로케일(locale)을 바꿔야 한다.
'''

import locale
from datetime import date
halloween = date(2019, 10, 31)
for lang_country in ['en_us', 'fr_fr',]:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime('%A, %B %d'))

#lang_country의 값
import locale
names = locale.locale_alias.keys()
good_names = [name for name in names if \
    len(name) == 5 and name[2] == '_']
print(good_names)