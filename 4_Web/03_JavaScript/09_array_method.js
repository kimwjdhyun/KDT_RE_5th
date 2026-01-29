let arr = [10, 20, 30, 40, 50];

console.log("원본 배열 : ", arr); // 원본 배열 :  (5) [10, 20, 30, 40, 50]

// 길이
console.log("길이 : ", arr.length); //  길이 :  5

// 요소 추가 (원본 변경 o)
arr.push(60); // 배열 가장 마지막에 추가
console.log("push(60) : ", arr); // push(60) :  (6) [10, 20, 30, 40, 50, 60]
arr.push(70, 80, 90, 100)
// 여러개 한 번에 추가 가능
console.log("push(60, 70, 80, 90, 100) : ", arr); // push(60, 70, 80, 90, 100) :  (10) [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

arr.unshift(0); // 배열 앞에 추가
console.log("unshift(0) : ", arr); // unshift(0) :  (11) [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

arr.unshift(-10, -20, -30); // 여러개 한번에 전달 가능하지만 매개변수에 전달한 순서대로 삽입
console.log("unshift(0) : ", arr); //unshift(0) :  (14) [-10, -20, -30, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

// 요소 삭제 (원본 변경 o)
let del1 = arr.pop(); // 배열 가장 끝 요소 삭제한 뒤 **삭제된 요소**를 반환
console.log("pop() : ", del1); // pop() :  100 
console.log("arr.pop() 원본 배열 출력 : ", arr); // arr.pop() 원본 배열 출력 :  (13) [-10, -20, -30, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

let del2 = arr.shift(); // 배열의 가장 처음 요소 삭제한 뒤 **삭제된 요소**를 반환
console.log("shift : ", del2); // shift :  -10
console.log("arr(원본 배열) : ", arr); // arr(원본 배열) :  (12) [-20, -30, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

//원본 유지가 필요한 경우 복사해놓고 사용함
let arr_copy = arr; 

// 슬라이싱 (원본 변경 x)
let sliced = arr.slice(1, 4);
console.log("arr sliced(1, 4) : ", sliced); // arr sliced(1, 4) :  (3) [-30, 0, 10]
console.log("arr(원본 배열) : ", arr); // arr(원본 배열) :  (12) [-20, -30, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

//splice : 기존 요소를 삭제 or 교체
let splice = arr.splice(1, 5, 15); // 1번째 인덱스부터 요소 5개 삭제, 그 자리에 15 추가
console.log("arr.spliced(1, 5, 15) : ", splice);  // arr.spliced(1, 5, 15) :  (5) [-30, 0, 10, 20, 30]
console.log("arr(원본 배열) : ", arr);  // arr(원본 배열) :  (8) [-20, 15, 40, 50, 60, 70, 80, 90]

arr.splice(2, 2); // 매개변수 두개만 작성하면, 첫 번째 매개변수 인덱스 부터 두 번째 매개변수 갯수까지 삭제만 진행
console.log("arr.splice : ", arr); // arr.splice :  (6) [-20, 15, 60, 70, 80, 90]

// 결합 // 문자열 메서드와 같은 방식 (원본 변경 x)
let arr2 = [10000, 20000];
console.log("concat : ", arr.concat(arr2)); // concat :  (8) [-20, 15, 60, 70, 80, 90, 10000, 20000]
console.log("arr(원본) : ", arr); // arr(원본) :  (6) [-20, 15, 60, 70, 80, 90]

// 탐색
console.log("indexOf : ", arr.indexOf('안')); //indexOf :  -1 : 배열안에 찾는 요소가 없으면 -1 반환 
console.log("indexOf : ", arr.indexOf(10000)); //원본 arr에는 10000이 없어서 -1 출력
console.log("indexOf : ", arr.indexOf(80)); // indexOf :  4
console.log("arr(원본) : ", arr); // arr(원본) :  (6) [-20, 15, 60, 70, 80, 90]

console.log("includes(80)", arr.includes(80)); // includes(80) true -> 포함 여부 불리언으로 반환

// 정렬
let nums = [5, 2, 8, 10, 388, 9];
nums.sort();
// 기본적으로 오름차순으로 정렬하며, 숫자의 크기가 아닌 문자의 앞글자 기준으로 정렬
console.log("배열 정렬 : ", nums); // 배열 정렬 :  (6) [10, 2, 388, 5, 8, 9]
nums.sort((a, b) => a - b);

// 숫자 기준 오름차순 정렬
console.log("nums.sort((a, b) => a - b) : ", nums); // nums.sort((a, b) => a - b) :  (6) [2, 5, 8, 9, 10, 388]

//내림차순 정렬
nums.sort((a, b) => b - a); // 내림차순
// 로직 자체가 b - a 라는 것은 숫자 기준으로 정렬하기 때문에 해당 숫자의 크기를 기준으로 정렬됨
console.log("nums.sort((a, b) => b - a) : ", nums); // nums.sort((a, b) => b - a) :  (6) [388, 10, 9, 8, 5, 2]

// 예시
let users = [
    {id : 1, name : "kimwjdhyun"},
    {id : 2, name : "choidmsjin"},
    {id : 4, name : "limwnsbeom"},
    {id : 6, name : "limdbhee"},
];

users.sort((a, b) => a.id - b.id);
console.log(users);
// {id: 1, name: 'kimwjdhyun'}
// {id: 2, name: 'choidmsjin'}
// {id: 4, name: 'limwnsbeom'}
// {id: 6, name: 'limdbhee'}

// 배열 순서 뒤집기
users.reverse();
console.log(users);
// {id: 6, name: 'limdbhee'}
// {id: 4, name: 'limwnsbeom'}
// {id: 2, name: 'choidmsjin'}
// {id: 1, name: 'kimwjdhyun'}

// => 원본 변형 o

// 배열의 순회

// map : 배열을 순회하면서 매개변수로 전달받은 콜백함수를 적용 (원본 변경 x)
nums = nums.map((x) => x * 2); // 각 요소를 한 번씩 선택해서 매개면수 (x)로 전달하고, 전달받은 x에 2를 곱해서 배열로 반환
console.log(nums); // (6) [776, 20, 18, 16, 10, 4]

// filter : callback 함수를 기준으로 요소를 필터링해서 반환
let filterd = nums.filter((x) => x > 15);
console.log(filterd); // (4) [776, 20, 18, 16]

//reduce : 앞 요소에 대해 뒤 요소를 연산한 결과를 누적
let sum = nums.reduce((acc, curr) => acc + curr, 0); // 두 번째 매개변수 받은 0에 배열을 순회하면서 앞 요소에 뒷 요소를 더한 값 반환
console.log(sum); // 844

let sum2 = 0;

for (let i = 0; i < nums.length; i++) {
    sum2 += nums[i];
    
}
console.log(sum2); // 844 위 reduce와 같음