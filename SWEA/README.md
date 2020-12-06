# Python 문제 풀이 재개

> 그동안 SSAFY 프로젝트에 너무 시간을 할애했습니다. 
>
> 틈을 내서라도 한 문제씩 풀어야했는데 제가 너무 풀어졌습니다. 
>
> 다시 시작해보겠습니다!!!



## 1949 : 등산로 조성

[문제링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE)

### 조건

1. 가장 높은 지점에서 시작한다.
2. 높은 지형에서 낮은 지형으로, 가로세로 방향으로 움직인다.
   1. 높이가 같거나 높으면 안되고, 대각선 방향도 안된다.
3. 딱 한 군데만 K 깊이만큼 지형변경이 가능하다.



### 작업 로그

결국 재귀를 잘 사용하는 것이 중요했습니다.

큰 문제 없이 해결했습니다. 

공사 이후 복구 코드를 잘 못된 위치에 둬서 비슷하지만 틀린 답이 나왔습니다.

해당 코드만 수정하니 Pass했습니다.

---

## 2382 : 미생물 격리

[문제링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl&categoryId=AV597vbqAH0DFAVl&categoryType=CODE)

### 조건

1. 구역의 모든 모서리는 약품이 있다.
   1. 미생물이 이동 중 약품에 닿으면 절반으로 수가 줄어들고 이동방향이 반대로 바뀐다.
2. 두 개 이상의 미생물 군집이 한 곳에 모이면 수는 합해지고 방향은 가장 큰 군집의 방향으로 정해진다.
3. M 시간 후 미생물의 총합을 출력한다.



### 작업 로그

그동안 흔히 해왔던 배열의 인덱스를 다루는 문제였습니다.

막혔던 부분은 군집이 3개 이상 합쳐질 때였습니다.

2개는 그냥 합치면 해결 가능했지만 3개 이상일땐 방향을 정하기 위해 최대 군집의 개수와 방향을 가지고 있었어야했습니다.

그 과정에서 배열 생성과 많은 반복문으로 인해 메모리와 실행시간이 크게 나왔지만 Pass 했습니다.

---



