// post func
async function send_post_request() { // param = data={}
    const response = await fetch('http://localhost:8000/tasks', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({id: 3, title:"make post-req", description: "do it!", tag: "ideas"}) // my param
    })

    const responseData = await response.json();
    console.log(responseData);
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
        result.data.forEach(element => {
            console.log(element.id, element.title);
        });
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

send_get_request()