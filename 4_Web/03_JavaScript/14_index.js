// callback 함수 사용 
console.log(1);
setTimeout(function () {
    console.log(2);
}, 2000);
console.log(3);

// 
// ex. 편의점 -> 음료를 고르고 -> 산다.

function goMart() {
    console.log('마트에서 어떤 음료를 살지 고민...');
}

function pickDrink() {
    //3초 고민 후에 결정
    setTimeout(function () {
        console.log('고민 끝!');
        product = '제로콜라';
        price = 2000;
    }, 3000);
}

function pay() {
    console.log(`상품명 : ${product}, 가격 : ${price}`);
}

let product;
let price;
goMart();
pickDrink();
pay();

///////////////////////

//1. 콜백 함수를 이용한 비동기 처리
function goMart() {
    console.log('마트에서 어떤 음료를 살지 고민...');
}

function pickDrink(callback) {
    //3초 고민 후에 결정
    setTimeout(function () {
        console.log('고민 끝!');
        product = '제로콜라';
        price = 2000;
        callback();
    }, 3000);
}

function pay() {
    console.log(`상품명 : ${product}, 가격 : ${price}`);
}

let product;
let price;
goMart();
pickDrink(pay);

//실습 1. callback hell
function call(name, cb) {
    setTimeout(() => {
        console.log(name);
        cb(name)
    }, 2000);
}

function back(cb) {
    setTimeout(() => {
        console.log('back');
        cb('back')
    }, 2000);
}

function hell(cb) {
    setTimeout(() => {
        cb('callback hell')
    }, 2000);
}

call('kim', function (name) {
    console.log(name + ' 반가워');
    back(function (txt) {
        console.log(txt + ' 을 실행했구나?');
        hell(function (message) {
            console.log('여기는 ' + message);
        });
    });
});