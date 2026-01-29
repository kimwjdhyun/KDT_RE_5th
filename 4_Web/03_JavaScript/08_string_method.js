let str = "              Hello JavaScript World          ";

console.log("원본 str", str); // 원본 str               Hello JavaScript World          

// .length : 길이 반환
console.log("길이 : ", str.length); // 길이 :  46
// 함수 x, 하나의 속성

// .trim : 공백 제거 // 원본 변경 x
console.log("공백 제거 : ",str.trim()); // 공백 제거 :  Hello JavaScript World

// .대소문자 변환 // 원본 변경 x
console.log("대문자 변환 : ", str.toUpperCase()); // 대문자 변환 :                HELLO JAVASCRIPT WORLD          
console.log("소문자 변환 : ", str.toLowerCase()); // 소문자 변환 :                hello javascript world         

// 탐색
console.log("글자 인덱스 찾기 : ", str.indexOf("J")); // 인덱스 찾기 :  20
console.log("단어 인덱스 찾기 : ", str.indexOf("Java")); // 첫번째 글자 기준으로 찾아줌, 없는 글자는 -1 출력

console.log("문자열의 포함 여부 확인 : ", str.includes("Java")); // 문자열의 포함 여부 확인 :  true -> 불리언으로 반환

// 슬라이싱 // 원본 변경 x
console.log("문자열 슬라이싱 : ", str.slice(6, 26)); // 문자열 슬라이싱 :          Hello JavaSc

// 치환 // 원본 변경 x
// 처음으로 나온 글자만 치환
console.log("한 글자 치환 : ", str.replace('l', 'e')); // 한 글자 치환 :                Heelo JavaScript World
// 단어를 치환     
console.log('한 단어 치환 : ', str.replace('World', 'Universe')); // 한 단어 치환 :                Hello JavaScript Universe    
// 전부 치환
console.log("전부 치환 : ", str.replaceAll('l', 'v')); // 전부 치환 :                Hevvo JavaScript Worvd          

// 분할 // 원본 변경 x
console.log("''분할 : ", str.split('')) // 모든 글자들이 한글자씩 잘려서 배열로 반환(공백 포함)
// ''분할 :  (46) [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'H', 'e', 'l', 'l', 'o', ' ', 'J', 'a', 'v', 'a', 'S', 'c', 'r', 'i', 'p', 't', ' ', 'W', 'o', 'r', 'l', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
console.log("' '분할 : ", str.split(' ')) // 공백 한칸(" ")을 기준으로 문자열로 나눠서 배열 반환
// ' '분할 :  (27) ['', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Hello', 'JavaScript', 'World', '', '', '', '', '', '', '', '', '', '']
console.log("l 기준 분할 : ", str.split('l')); // 분할 기준인 'l'은 사라지고 배열로 만들어져 반환
// l 기준 분할 :  (4) ['              He', '', 'o JavaScript Wor', 'd          ']

// 합치기 // 원본 변경 x
let str2 = "with Javascript";
console.log("문자열 합치기1 : ", str.concat(str2)); // 문자열 합치기 :                Hello JavaScript World          with Javascript

console.log(`문자열 합치기 2 : ${"Hello ".concat(str2)}`); // 문자열 합치기 2 : Hello with Javascript
console.log(`문자열 합치기 3 : ${"Hello ".concat(str2, str)}`); // 문자열 합치기 3 : Hello with Javascript              Hello JavaScript World 
console.log(`문자열 합치기 4 : ${"Hello ".concat("i am kinwjdhyun "," nice to meet you")}`); // 문자열 합치기 4 : Hello i am kinwjdhyun  nice to meet you

