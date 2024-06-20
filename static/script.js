// script.js
document.addEventListener("DOMContentLoaded", function() {
    // localStorage.setItem('total_score', 0);

    const qscore=[10,20,30,20,30]
    let qflag = JSON.parse(localStorage.getItem('qflag')) || [false, false, false, false, false];

    function fetchScore() {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', '/get_score', true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                const total_score = response.score || 0;
                localStorage.setItem('total_score', total_score);
                updateScoreDisplay();
            }
        };
        xhr.send();
    }

    //Displaying total score
    function updateScoreDisplay() {
        let total_score = parseInt(localStorage.getItem('total_score')) || 0;
        const scoreDisplay = document.getElementById("score");
        if (scoreDisplay) {
            scoreDisplay.textContent = `Total Score: ${total_score}`;
        }
    }
    // updateScoreDisplay();
    fetchScore();

    //Defining the code drag operation for questions 1,2, and 3
    const codeBlock = document.querySelectorAll(".code-block");
    const pickArea = document.getElementById("pickArea");
    const dropArea = document.getElementById("dropArea");

    codeBlock.forEach(block => {
        block.addEventListener("dragstart", dragStart);

    });
    function dragStart(e) {
        let selected = e.target;
        dropArea.addEventListener("dragover",function(e){e.preventDefault();});
        dropArea.addEventListener("drop",function(e){dropArea.appendChild(selected); selected=null;})
        pickArea.addEventListener("dragover",function(e){e.preventDefault();});
        pickArea.addEventListener("drop",function(e){pickArea.appendChild(selected); selected=null;})
    }

    //Function to update score and qflag
    function updateScoreAndFlag(questionId) {
        alert("You cracked it!!!");
        if (!qflag[questionId - 1]) {
            let total_score = parseInt(localStorage.getItem('total_score')) || 0;
            total_score += qscore[questionId - 1];
            localStorage.setItem('total_score', total_score);
            qflag[questionId - 1] = true;
            localStorage.setItem('qflag', JSON.stringify(qflag));
            // AJAX request to update score in the database
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/update_score', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    console.log('Score updated successfully');
                } else {
                    console.error('Failed to update score');
                }
            };
            const username = '{{ session["username"] }}';
            xhr.send(JSON.stringify({ username: username, score: total_score }));
        } else {
            alert("You have already submitted this question. Your score will not be updated.");
        }
    }

    //Checking answers for questions 1,2 and 3
    window.submitCodeOrder = function() {
        const questionId = window.location.pathname.split('/').pop();
        // Question 4 answer checking
        if (questionId == 4) {
            const userInput2 = document.getElementById("userInput1").value;
            const correctAnswer4 = "Htruqjcnyd 5159!";
            if (userInput2 === correctAnswer4) {
                updateScoreAndFlag(4);
            } else {
                alert("Incorrect answer!");

            }
            updateScoreDisplay();
            return;
        }

        // Question 5 answer checking
        if (questionId == 5) {
            const userInput2 = document.getElementById("userInput2").value;
            const correctAnswer5 = "BANC";
            if (userInput2 === correctAnswer5) {
                updateScoreAndFlag(5);
            } else {
                alert("Incorrect answer!");
            }
            updateScoreDisplay();
            return;
        }
        let max=0;
        const codeBlock=document.querySelectorAll(".code-block");
        codeBlock.forEach(block=>{
            let temp=parseInt(block.getAttribute('data-order'));
            if(temp>max){
                max=temp;
            }
        })
        const order = [];
        dropArea.querySelectorAll(".code-block").forEach(block => {
            order.push(parseInt(block.getAttribute('data-order')));
        })
        let isCorrect = true;
        for (let i = 0; i < max; i++) {
            if (order[i] !== i + 1) {
                isCorrect = false;
                qflag[questionId - 1] = true;
                alert("The order is incorrect!")
                break;
            }
        }
        if (isCorrect) {
            updateScoreAndFlag(questionId);
        }
        updateScoreDisplay();

    }

});



