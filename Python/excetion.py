class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg= msg
    def __str__(self):
        return "[오류 코드 001] " + self.msg

try:
    print("나누기 전용 계산기입니다")
    nums=[]
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    # nums.append(int(nums[0]/nums[1]))
    if nums[0] >= 10 or nums[1] >= 10:
        raise BigNumberError("입력값: {0}, {1}".format(nums[0], nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("오류 발생!")
except BigNumberError as err:
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("수행 종료")
# except Exception as err:
#     print("알수없는 오류")
#     print(err)