
const form = document.getElementById("configurations-form")
form.addEventListener("submit", onFormSubmit)

async function onFormSubmit(event) {
    // prevent the default "submit" action happening
    event.preventDefault();

    // pull data from the form
    const formData = new FormData(event.target);

    // create map and fill it in with formData
    let map = {};
    formData.forEach((value, key) => {
        map[key] = value;
    });

    // convert map to json string
    const json = JSON.stringify(map)

    // submit json to API
    const response = await fetch("/config", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: json
    })

    // log response
    console.log(response)
}
