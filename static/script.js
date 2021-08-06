mainPage = document.getElementById('main')

const getData = async (data) => {
    
    try{
    const response = await fetch('https://app.ticketmaster.com/discovery/v2/events?apikey=7elxdku9GGG5k8j0Xm8KWdANDgecHMV0&locale=*&page=100'
    )
    const data = await response.json()
    console.log(data)
    // console.log(data._embedded.events[0].name)
    
    renderData(data)

    
   
} catch (err){
    console.error(err)
}

}

const renderData = (data) => {

    for (let i = 0; i < data._embedded.events.length; i++){
        // console.log(data._embedded.events[i].name)

        // const dataHTML = `
        // <h1>${data._embedded.events[i].name}</h1>`

        mainPage.innerHTML += 
        `
        <img src= '${data._embedded.events[i].images[8].url}' width='300' height='200'>
        <h3>${data._embedded.events[i].name}</h3>
        <p> Date: ${data._embedded.events[i].dates.start.localDate}</p>

        <form action='/submit' method='POST'>

            <div class='userEntry'>
                <input
                    type='text'
                    name='username'
                    placeholder='Your Name'
                />
            </div>

            <div class='userEntry'>
                <textarea 
                    name='comments'
                    id=''
                    cols='60'
                    rows='20'
                    placeholder='Post your comments here!'
                ></textarea>
            </div>
            <input type='submit' value='Submit' class='submitButton' />
        </form>

        <hr></hr>
        `
    }

}


getData()


