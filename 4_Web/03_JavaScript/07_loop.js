// 1. for문
// 횟수를 기준으로 하는 반복문

console.log("========= for반복문 =========");

for (let i = 0; i < 10; i++){
    console.log(i);
}

console.log("-----------------")

for (let i = 10; i >= 1; i--){
    console.log(i);
}

console.log("-----------------")

for (let i = 0; i <= 20; i+=3){
    console.log(i);
}

console.log("-----------------")
// 1부터 100까지의 합 구하기
// let sum = 0;
// for (let i = 1; i < 101; i++){
//     sum += i;
// }
// console.log("1에서 100까지의 합", sum);

// 실습 1. 10000까지의 숫자 중에서 13의 배수이면서 홀수인 숫자를 찾아보기
// 조건 : prompt를 이용해서 입력받은 수 까지 13의 배수이면서 홀수인 숫자를 찾기

// for (let i = 1; i <= 10000; i++) {
//     if (i % 13 === 0 && i % 2 === 1) {
//         console.log(i);
//     }
// }

// // 조건 포함(prompt 사용)
// let num = Number(prompt("숫자를 입력하세요."));

// for (let i = 1; i <= num; i++) {
//     if (i % 13 === 0 && i % 2 === 1) {
//         console.log(i);
//     }
// }

// 이중 for 문

console.log("========= 이중 for 문 ==========")

for (let i = 0; i < 3; i++) {
    // i는 고정된 상태로 j 만 1씩 커지면서 해당 scope의 코드 실행됨
    // j의 루프가 완료되면 i가 1씩 커지는 것
    for(let j = 0; j < 5; j++){
        console.log("i : ",i, "j : ", j);
    }
}

// 실습 2. 구구단 만들기

// for (i = 1; i < 10; i++) {
//     console.log(`===${i}단===`)
//     for (j  = 1; j < 10; j++) {
//         console.log(`${i} x ${j} = ${i * j}`);
//     }
// }

// //2. while 문
// // 조건을 기준으로 반복

// console.log("========= while문 =========")

// let i = 0;

// while ( i < 5) {
//     console.log(i);
//     i++ // i++없다면 무한루프
// }

// // 초록불일 때만 콘솔을 찍는 로직
// let blinker = "초록불";

// while (blinker === "초록불") {
//     console.log("길을 건너세요!");
//     blinker = prompt('신호등 상태를 입력하세요 (초록불 / 빨간불)');
//     // 예외처리
//     if (blinker === "초록불") {
//         continue;
//     } else if(blinker === "빨간불") {
//         break;
//     } else {
//         blinker = prompt("신호등 상태를 다시 입력하세요 (초록불 / 빨간불)");
//     }
// }

// 실습 0 ~ 100의 숫자 중에서 2 또는 5의 배수 총합 구하기
let sum = 0;
let num = 0;

while (num < 101) {
    if (num % 2 === 0 || num % 5 === 0) {
        sum += num;
    }
    num++;
}
console.log(sum);