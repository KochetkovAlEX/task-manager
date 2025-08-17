
const form = document.querySelector('form')

form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Получаем значения полей
    const tag = document.getElementById('tag').value;
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    
    if(create_and_add_tasks(tag, title, description)){
        // очищаем форму
        this.reset();
    
        // Показываем уведомление об успехе (UIKit notification)
        UIkit.notification({
            message: 'Form submitted successfully!',
            status: 'success',
            pos: 'top-right',
            timeout: 5000
        });
    }
    
    
});



// create tasks 
// *TODO: Add params for function!
function create_and_add_tasks(tag, text, description){
    // const task_container = document.getElementById("tasks_id");
    // const newElem = document.createElement('div')
    // newElem.className = "uk-card uk-card-default uk-card-body uk-margin-top"
    
    // const new_tag = document.createElement("div")
    // new_tag.className = "uk-card-badge uk-label"
    // new_tag.textContent = tag

    // const new_title = document.createElement('h3')
    // new_title.className = "uk-card-title";
    // new_title.textContent = text

    // const new_p = document.createElement('p')
    // new_p.textContent = description

    // newElem.appendChild(new_tag)  
    // newElem.appendChild(new_title)
    // newElem.appendChild(new_p)
    // task_container.appendChild(newElem)

    if (!tag.trim() || !text.trim()) return false;
    
    const task_container = document.getElementById("tasks_id");
    
    const taskCard = `
        <div class="uk-card uk-card-default uk-card-body uk-margin-top uk-width-1-2@m">
            <div class="uk-card-badge uk-label">${tag}</div>
            <h3 class="uk-card-title">${text}</h3>
            <p>${description}</p>
            <div class="uk-text-meta">${new Date().toLocaleString()}</div>
        </div>
    `;
    
    task_container.insertAdjacentHTML('afterbegin', taskCard);
    return true;
}

// const add_btn = document.getElementById('add_btn')
// add_btn.addEventListener('click', ()=>{
//     console.log(1)
//     create_and_add_tasks()
// })