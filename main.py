# 파일이름 :
# 작 성 자 :
1. 시나리오 제목
해외직구 신발 사이즈 마스터 v1.0 : 실패 없는 쇼핑 조력자

2. 과제 수행 소감 
평소 해외 직구를 할 때마다 복잡한 사이즈 표기 때문에 고민이 많았는데, 
수업 시간에 배운 파이썬의 리스트와 조건문을 활용해 직접 변환기를 만들어보니 코딩이 실생활 문제를 해결하는 유용한 도구라는 것을 깨달았습니다. 
특히 AI 파트너와 협업하며 제가 놓치기 쉬운 
'복합 대입 연산자'나 '논리 연산자'의 활용법을 다시 한번 점검할 수 있어 학습 효율이 높았습니다.
v1.0 뼈대 코드를 완성하며 데이터가 어떻게 저장되고 처리되는지 흐름을 확실히 이해하게 되었습니다.

user_name = input("프로그램 사용자의 이름을 입력하세요: ")
size_list = []
is_active = True
total_count = 0
VERSION = 1.0

print(f"\n--- {user_name}님의 해외직구 사이즈 변환기 (v{VERSION})를 시작합니다 ---")

fori inrange(1, 4): 
print(f"\n[{i}/3 번째 사이즈 입력]") 
user_input = input("변환할 한국 신발 사이즈(mm)를 입력하세요 (종료는 0): ")


mm_size = int(user_input)

ifmm_size == 0: 
print("사용자에 의해 입력을 종료합니다.")
Break

ifmm_size < 150ormm_size > 350: # 논리 연산자(or) 활용
print("입력 오류: 150mm ~ 350mm 사이의 값만 입력 가능합니다.")
Continue

size_list.append(mm_size) 
total_count += 1

print("\n"+ "="*50) 
print(f" 총 {total_count}개의 사이즈가 성공적으로 입력되었습니다.") 
print("="*50)

forsize insize_list:
us_result = (size - 180) / 10+ 4.0
eu_result = (size / 10) + 10.0

ifsize >= 280: 
category = "빅사이즈 (재고 확인 필수)"
elifsize >= 230andsize < 280:
category = "일반 성인 사이즈"
else:
category = "키즈/아동 사이즈"

print(f"▶ 한국: {size}mm | 미국(US): {us_result}| 유럽(EU): {eu_result}| 판정: {category}")


iflen(size_list) > 0: 
avg_size = sum(size_list) / len(size_list) 
print("\n"+ "-"*50) 
print(f"[최종 분석 데이터 요약]") 
print(f"1. 전체 조회 횟수: {len(size_list)}건") 
print(f"2. 입력된 사이즈 합계: {sum(size_list)}mm") 
print(f"3. 가장 큰 사이즈: {max(size_list)}mm") 
print(f"4. 가장 작은 사이즈: {min(size_list)}mm") 
print(f"5. 전체 평균 사이즈: {avg_size:.1f}mm") 

print("-"*50) else: print("\n분석할 데이터가 없습니다.") 

print(f"\n{user_name}님, 이용해 주셔서 감사합니다. 즐거운 쇼핑 되세요!")
