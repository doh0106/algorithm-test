# **최소 예시: 하나의 파일로 TDD + 시공간 측정 + 로깅**

## 1) 데코레이터 정의

먼저, 한 파일 내부에 **데코레이터**들을 정의합니다.

```python
import time
import tracemalloc

def measure_performance(func):
    """
    실행 시간과 메모리 사용량을 측정하는 데코레이터
    """
    def wrapper(*args, **kwargs):
        tracemalloc.start()              # 메모리 추적 시작
        start_time = time.perf_counter() # 시간 측정 시작

        result = func(*args, **kwargs)   # 실제 함수 실행

        end_time = time.perf_counter()   
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"[Perf] {func.__name__}")
        print(f"  - Time: {end_time - start_time:.6f} s")
        print(f"  - Current Mem: {current / 1024:.2f} KB")
        print(f"  - Peak Mem: {peak / 1024:.2f} KB\n")

        return result
    return wrapper

def log_input_output(func):
    """
    함수 호출 시 입력값, 출력값을 로깅해주는 데코레이터
    """
    def wrapper(*args, **kwargs):
        print(f"[Logger] Calling: {func.__name__}")
        if args or kwargs:
            print(f"  - Inputs: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  - Output: {result}\n")
        return result
    return wrapper
```

- `measure_performance`: 함수의 **실행 시간**과 **메모리 사용량**을 출력  
- `log_input_output`: 함수의 **이름**, **입력 인자**, **출력 결과**를 출력  

---

## 2) TDD 방식 테스트 함수

온라인 코딩 테스트 플랫폼에선 보통 **`unittest`** 같은 라이브러리를 자유롭게 못 쓰거나,  
**별도 파일**로 분리하기 힘들 수 있습니다.  

따라서 **직접 테스트 함수를 만들어** 쓰는 방식을 간단히 예시로 들어보겠습니다.

```python
def run_tests():
    """
    간단한 TDD를 위한 테스트 함수
    - 실패 시 AssertionError 발생
    - 성공 시 별도의 메시지 없이 넘어감
    """
    # 1) 테스트 케이스 1
    nums = [1, 2, 3, 4, 5]
    assert solution(nums) == 6, "Test Case 1 Failed"

    # 2) 테스트 케이스 2
    nums = []
    assert solution(nums) == 0, "Test Case 2 Failed"

    # 3) 테스트 케이스 3
    nums = [2, 4, 6, 8]
    assert solution(nums) == 20, "Test Case 3 Failed"

    # 4) 테스트 케이스 4
    nums = [1, 3, 5, 7]
    assert solution(nums) == 0, "Test Case 4 Failed"

    print("All tests passed!")  
```

- 여기서 `assert solution(nums) == ...` 형태로 테스트.  
- 하나라도 틀리면 **AssertionError**로 어떤 테스트가 실패했는지 알 수 있음.

---

## 3) 실제 솔루션 함수

문제 예시:  
- **"주어진 배열에서 짝수만 골라 합을 구하라"**  

```python
@measure_performance
@log_input_output
def solution(nums):
    """
    짝수만 합산하여 반환.
    """
    return sum(x for x in nums if x % 2 == 0)
```

- **데코레이터 두 개**를 동시에 달아서,  
  - 함수가 호출될 때 **함수명, 입력, 출력** 로깅  
  - 실행 시간과 메모리 사용량 측정

---

## 4) 메인 실행부

온라인 코딩 테스트에서는 보통 **`solve()`** 또는 **`main()`** 같은 함수를 호출하거나,  
바로 코드가 시작되지만, 여기서는 예시로 `if __name__ == "__main__":` 부분을 두겠습니다.

```python
if __name__ == "__main__":
    # 1) TDD 방식: 테스트 먼저 실행
    run_tests()  # 테스트 통과 여부 확인

    # 2) 코딩테스트 플랫폼에서의 최종 제출은 보통 입력/출력을 한다고 가정.
    #    (예: 백준처럼 입력을 받고, print() 하는 로직)
    #    여기서는 간단하게 직접 실행해봅시다.

    # 임의 테스트 입력
    print("\n[Manual Check]")
    arr = [10, 11, 12, 13]
    answer = solution(arr)
    print(f"Final Answer: {answer}")
```

### 실행 흐름
1. `run_tests()`로 **테스트 케이스**들을 검증  
   - 전부 통과하면 "All tests passed!" 출력  
   - 실패 시 assertion error로 어느 케이스가 틀렸는지 확인  
2. 수동으로 한 번 더 `solution()` 호출해서 최종 동작 확인  

---

# **최종 요약**

1. **데코레이터**  
   - `@measure_performance`: 시간·메모리  
   - `@log_input_output`: 함수명·입출력  
2. **TDD 테스트 코드**(간단히 직접 구현)  
   - `run_tests()` 함수에 **assert**로 케이스 확인  
3. **실제 `solution()` 함수**  
   - 문제를 해결하는 핵심 로직  
   - 데코레이터 적용  
4. **메인 실행부**  
   - 테스트 → (성공 시) 추가 실행

이렇게 **한 파일**에 모두 넣으면,  
- **온라인 코딩 테스트 환경**에서도 함수 입출력, 시공간 성능을 빠르게 확인  
- **TDD** 방식으로 문제 풀이 안정성을 높임  

원하시는 경우,  
- `run_tests()`는 제출 직전에 **주석 처리**하거나,  
- 제출 코드만 **별도 복사** 해서 사용하시면 됩니다.

**이것만 보고 따라해도**  
- 간단한 **TDD** 적용,  
- **시공간 측정**,  
- **로깅**  
을 한 번에 경험할 수 있으니 참고해서 활용해보세요! 