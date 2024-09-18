document.getElementById('response-form').addEventListener('submit', function(e) {
    console.log("submit...")
    e.preventDefault();
    let answerText = document.getElementById('answer').value;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/score?answer=' + encodeURIComponent(answerText), true);
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
            var score = xhr.responseText.trim();
            document.getElementById('last-answer').textContent = answerText;
            document.getElementById('score').textContent = score;
            document.getElementById('answer').value = '';
        } else {
            alert('通信に失敗しました。');
        }
    };
    xhr.onerror = () => alert('通信に失敗しました。');
    xhr.send();
});