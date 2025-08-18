// post func
async function send_post_request() { // param = data={}
    const response = await fetch('http://localhost:8000/tasks', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({title:"make post-req", description: "do it!", tag: "ideas"}) // my param
    })

    const responseData = await response.json();
    return await responseData;
}

send_post_request()

// get func
async function send_get_request() {
    try {
        const response = await fetch('http://localhost:8000/tasks');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        return result
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

document.addEventListener('DOMContentLoaded', async () => {
    try {
        const tasks = await send_get_request();
        tasks.forEach(task => {
            create_and_add_tasks(task.tag, task.title, task.description);
        });
    } catch (error) {
        console.error("Could not load tasks:", error);
    }
});