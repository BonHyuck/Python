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