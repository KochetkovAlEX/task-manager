
const add_btn = document.getElementById('add_btn')
add_btn.addEventListener('click', ()=>{
    console.log(1)
    create_and_add_tasks()
})


function create_and_add_tasks(){
    const task_container = document.getElementById("tasks_id");
    const newElem = document.createElement('div')
    newElem.className = "uk-card uk-card-default uk-card-body uk-margin-top"
    
    const new_title = document.createElement('h3')
    new_title.className = "uk-card-title";
    new_title.textContent = "Test Title"

    const new_p = document.createElement('p')
    new_p.textContent = 'Test text'

    newElem.appendChild(new_title)
    newElem.appendChild(new_p)
    task_container.appendChild(newElem)
}