
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
    })
}