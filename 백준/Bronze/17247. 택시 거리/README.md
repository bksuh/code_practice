# [Bronze I] 택시 거리 - 17247 

[문제 링크](https://www.acmicpc.net/problem/17247) 

### 성능 요약

메모리: 32412 KB, 시간: 176 ms

### 분류

사칙연산, 기하학, 수학

### 제출 일자

2024년 12월 20일 16:35:20

### 문제 설명

<p style="text-align: center;"><img alt="" src=""></p>

<p>택시 거리는 바둑판 모양의 도로망을 가진 도시에서 점 A에서 B까지의 최단 거리를 구할 경우 도로를 따라서만 가는 가장 짧은 거리를 뜻한다.</p>

<p>위의 사진에서는 빨간색 선이 택시거리이다. 즉, 점 A의 좌표가 (x<sub>1</sub>, y<sub>1</sub>)이고 점 B의 좌표를 (x<sub>2</sub>, y<sub>2</sub>)라고 했을 때, 두 장소 사이의 택시 거리 D는 다음과 같다.</p>

<p>\(D = |x_2 - x_1| + |y_2 - y_1|\)</p>

<p>인접한 0과 0, 0과 1, 1과 1 사이의 거리를 1이라고 할 때, 두 1 사이의 거리를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 줄엔 문자열의 높이 N과 가로 M이 주어진다. (2 ≤ N, M ≤ 1,000) 이다.</p>

<p>두 번째 줄부터 M개의 숫자 0또는 1이 예제 입력과 같이 N개의 줄에 걸쳐 입력된다.</p>

<p>1는 항상 두 개만 입력된다.</p>

### 출력 

 <p>주어진 숫자들에서 1과 1사이의 택시 거리를 구하시오.</p>

