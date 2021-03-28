let my_receivers = []

function remove_receiver(id){
	
	delete my_receivers[id]
	console.log(my_receivers)

	display_receivers()
}

function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function display_receivers(){
	if (my_receivers.length == 0){
		return null
	}
	let receivers_div = document.getElementById('receivers')
	receivers_div.innerHTML = ""

	for (var i = 0; i < my_receivers.length; i++) {
		receivers_div.innerHTML += `<div class="receiver_item">${my_receivers[i]}<button id="${i}" onclick="remove_receiver(this.id)" class="remove_button">Remover</button></div><br><br>`
	}
}

function add_receiver(){
	let receiver = document.getElementById('receiver')
	
	if (validateEmail(receiver.value) == false){
		alert('Endereço de email nulo ou inválido!')
	}
	else if (my_receivers.includes(receiver.value)) {
		alert('Endereço de email já adicionado à lista!')
	}
	else {
		let receivers_div = document.getElementById('receivers')		
		my_receivers.push(receiver.value)

		display_receivers()

		console.log(my_receivers)
	}

	receiver.value = ""
}

