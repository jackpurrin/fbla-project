function start() {
    let type = prompt("Do you want a cat or a dog?")
    let name = prompt("Set your pets name", "")

    console.log(type)
    console.log(name)

    document.getElementById("pet").src="assets/img/cat.jpg";
}