function cal() {
    const value1 = document.getElementById('value1').value;
    const value2 = document.getElementById('value2').value;
    const operator = document.getElementById('operator').value;
    const result = document.getElementById('result');

    if (value1 === '' || value2 === '') {
        result.value = '값을 모두 입력해주세요!';
        return;
    }

    if (operator === '') {
        result.value = '연산자를 입력해주세요!';
        return;
    }

    const num1 = Number(value1);
    const num2 = Number(value2);

    let answer;

    if (operator === '+') {
        answer = num1 + num2;
    } else if (operator === '-') {
        answer = num1 - num2;
    } else if (operator === '*') {
        answer = num1 * num2;
    } else if (operator === '/') {
        if (num2 === 0) {
            result.value = '0으로 나눌 수 없습니다!';
            return;
        }
        answer = num1 / num2;
        } else {
        result.value = '올바른 연산자를 입력하세요! (+, -, *, /)';
        return;
        }

        result.value = answer;
    }
    function resetInput() {
        document.getElementById('value1').value = '';
        document.getElementById('value2').value = '';
        document.getElementById('operator').value = '';
        document.getElementById('result').value = '';
}