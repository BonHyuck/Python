# SWEA D2 리뷰

## 코드 보기

- [1859.py - 사재기 최대값](https://github.com/BonHyuck/Python/blob/master/D2/1859.py)

- [1926.py - 369 게임](https://github.com/BonHyuck/Python/blob/master/D2/1926.py)
- [1954.py - 달팽이](https://github.com/BonHyuck/Python/blob/master/D2/1954.py)
- [1979.py - 낱말 퍼즐](https://github.com/BonHyuck/Python/blob/master/D2/1979.py)
- [1983.py - 성적 보여주기](https://github.com/BonHyuck/Python/blob/master/D2/1983.py)
- [1984.py - 평균값 구하기](https://github.com/BonHyuck/Python/blob/master/D2/1984.py)
- [1986.py - 더하기빼기](https://github.com/BonHyuck/Python/blob/master/D2/1986.py)
- [2001.py - 파리 잡기](https://github.com/BonHyuck/Python/blob/master/D2/2001.py)
- [2005.py - 파스칼 삼각형](https://github.com/BonHyuck/Python/blob/master/D2/2005.py)
- [2007.py - 단어가 도는지](https://github.com/BonHyuck/Python/blob/master/D2/2007.py)

## 소감

전체적으로 D2는 많이 어렵지는 않았다. 배열이나 내장함수를 잘 사용하면 충분히 풀 수 있었으며 알고리즘 자체도 어려운 것은 많이 없었습니다.

주로 배열 초기값 설정과 이후 흐름에 대해서 파악하면 풀리는 문제들이 많았습니다.

위의 문제들이 D2의 전부는 아니라는 점 양해바랍니다. D2 풀던 중간부터 깃을 활용하기 시작해서...



## 1859.py - 사재기 최대값

- [코드 보기](https://github.com/BonHyuck/Python/blob/master/D2/1859.py)

정수로 이루어진 하나의 긴 배열이 주어집니다. 각 배열의 요소는 하루의 물건 가격을 나타내고 문제에 나오는 주인공은 팔 것인지 살 것인지 결정하며 모든 날짜가 지난 이후 주인공이 얻게 되는 최대 이익을 산출하는 문제였습니다.

이 문제는 개인적으로 D2에서 가장 어려운 문제였다고 생각합니다. 어느 시점에 팔아야 최대값이 나오는지 구상하는 것이 제일 어려웠습니다.

**첫 번째 접근법**은 해당 원소의 양 옆을 검사하여 양 옆보다 큰 값일 경우 판매하며 그러지 않을 경우 구입하는 것이였습니다. 하지만 모든 원소를 검사하다보니 메모리 에러가 발생하여 실패했습니다.

결국 모든 입력값을 프로그램 없이 제가 검토하여 새로운 접근법을 찾기 시작했습니다.

**두번째 접근법**은 배열 내 최대값을 구해서 최대값 이외에는 전부 구입하고 최대값에만 구입하게 했습니다. 그러다보니 최대값이 앞에 나오는 경우 구입 수량이 얼마 되지 않았고 이윤도 적게 나왔으며 뒤에 원소에 대해서는 계산이 진행되지 않았습니다. 

두번째 접근법의 실패로 **세번째 접근법**, 지금의 코드가 도출됐습니다. 최대값을 구하고 딱 최대값 전까지 구입, 최대값에서 판매한 후 앞에 계산이 된 배열은 버리고 뒤에 남은 배열에 대해 다시 최대값을 구했습니다. 같은 작업을 배열의 길이가 1이 될때까지 반복하여 최종 값을 도출했습니다.



## 1926.py - 369 게임

[코드 보기](https://github.com/BonHyuck/Python/blob/master/D2/1926.py)

하나의 정수가 주어집니다. 1부터 해당 정수까지 나오는 숫자 중 3, 6, 혹은 9가 들어가는 번호에서 3, 6, 9의 개수만큼 `-` 를 출력하는 문제입니다.

이렇게 풀어도 되나 싶을 정도로 쉬운 문제였습니다. 파이썬의 편리함이 힘을 발휘하는 코드였습니다.

내장함수인 `str`을 사용하여 숫자를 문자화해서 문자에 들어있는 3, 6, 9를 세서 결과에 붙여주기만 하는 코드를 작성했습니다.





