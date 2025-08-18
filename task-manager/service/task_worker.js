
const form = document.querySelector('form')

form.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Получаем значения полей
    const tag = document.getElementById('tag').value;
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    
    if(create_and_add_tasks(tag, title, description)){
        await send_post_request(tag, title, description);

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


    if (!tag.trim() || !text.trim()) return false;
    
    const task_container = document.getElementById("tasks_id");
    
    const taskCard = `
        <div class="uk-card uk-card-default uk-card-body uk-margin-top">
            <div class="uk-card-badge uk-label">${tag}</div>
            <h3 class="uk-card-title">${text}</h3>
            <p>${description}</p>
            <div class="uk-text-meta">${new Date().toLocaleString()}</div>
        </div>
    `;
    
    task_container.insertAdjacentHTML('afterbegin', taskCard);
    return true;
}

