window.onload = () => {
    updateWeeklyProgressBar()
    // TODO: Implement updateDailyProgressBar()
    updateDailyProgressBar() 
}

// add event listener to all the checkboxes to update with the database in real time
buttons = document.getElementsByClassName('form-check-input');
for(let i = 0; i < buttons.length; i++){
    buttons[i].addEventListener('click', ()=> {
        let data = {"task": buttons[i].value, "day": buttons[i].name};

        fetch("/updateDailyTask", {
            method: "PATCH",
            headers: {'Content-Type': 'application/json'}, 
            body: JSON.stringify(data)
        }).then(res => {
            console.log("Request complete. Response:", res);
        });



        updateWeeklyProgressBar()
        updateDailyProgressBar() 
    })
}

// updates the width of the progress bar element
function updateWeeklyProgressBar() {
    var elem = document.getElementById("weeklyProgressBar");

    let buttonsChecked = 0;
    for(let j = 0; j < buttons.length; j++){
        if (buttons[j].checked){
            buttonsChecked++;
        }
    }

    var new_width = Math.round(buttonsChecked / buttons.length * 100);

    elem.style.width = new_width + "%";
    elem.innerText = new_width + "%";
}

// updates the width of the progress bar element
function updateDailyProgressBar() {
    var elem = document.getElementById("dailyProgressBar");
    const d = new Date();
    let day = d.getDay(Date.now());
    
    if(day === 0){
        day = 6;
    }
    else{
        day -= 1;
    }

    let buttonsChecked = 0;
    for(let j = day; j < buttons.length; j = j + 7){
        if (buttons[j].checked){
            buttonsChecked++;
        }
    }
 
    var new_width = Math.round((buttonsChecked / (buttons.length / 7)) * 100);

    elem.style.width = new_width + "%";
    elem.innerText = new_width + "%";
}