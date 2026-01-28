let pansoli = {
    name : "이몽룡",
    age : 18,
    like : ["강아지", "고양이"],
    isMarried: true,
    girlfriend: {name: '성춘향', age: 16}
};

console.log("춘향전", pansoli);

let mathScore = "77";
let engScore = "88";

let avgScore = (Number(mathScore) + Number(engScore)) / 2;

console.log("수학 점수", mathScore.toString(), "점");
console.log("영어 점수", engScore.toString(), "점");
console.log("평균 " + avgScore + "점")


let mathScore1 = prompt('수학점수 입력');
let engScore1 = prompt('영어점수 입력');
let avgScore1 = (Number(mathScore1) + Number(engScore1)) / 2;
alert(`평균 점수 ${avgScore1}점 입니다.`)