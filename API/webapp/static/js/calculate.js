 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
async function makeRequest(url, method='GET', body) {
    let headers={
        'X-CSRFToken': getCookie('csrftoken')
    }
let response = await fetch(url, {method, headers:headers, body:body});

if (response.ok) {  // нормальный ответ
    return await response.json();
} else {            // ошибка
    let error = new Error(response.statusText);
    error.response = response;
    throw error;
}
}

async function calculateIntegers(event) {
    event.preventDefault()
    let url = event.target.dataset.url
    let a = document.getElementById('value1').value
    let b = document.getElementById('value2').value
    let data = {"A": a, "B": b}

    try{
        let result = await makeRequest(url, "POST", JSON.stringify(data))
        let r = document.getElementById('result')
        r.innerText = result.result
    }
    catch(e){
        console.log(e);
    }

}

async function getToken(){
    await makeRequest("/calculation/get_token/")
}

window.addEventListener('load', getToken)
