function generateLink() {
    var links = ["https://integro.biblioteka.gliwice.pl/692300247875/king-stephen/stephen-king-na-wielkim-ekranie?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692800373413/atwood-margaret/opowiesc-podrecznej?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692900393764/ng-celeste/male-ogniska?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692900391565/kwan-kevin/bajecznie-bogaci-azjaci?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692300294163/lee-harper/zabic-drozda?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692500337134/lynch-scott/klamstwa-lockea-lamory?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/693300470131/gabaldon-diana/powiedz-pszczolom-ze-odszedlem?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692300248008/garcia-marquez-gabriel/sto-lat-samotnosci?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692300280100/fitzgerald-francis-scott/wielki-gatsby?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692300193539/woolf-virginia/pani-dalloway?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692300273659/kerouac-jack/w-drodze?bibFilter=69",
                 "https://integro.biblioteka.gliwice.pl/692500334870/christie-agatha/morderstwo-w-orient-expressie?bibFilter=69",
    ]
    var randomIndex = Math.floor(Math.random() * links.length);
    document.getElementById("link").value = links[randomIndex]
}


function loadIndicator(){
    load = 0
    document.getElementById("loadIndicator").classList.remove("d-none")
    var loadValue = document.getElementById("loadValue")

    setInterval(function(){
      $.ajax({
        type: 'GET',
        url: `url-count/`,
        success: function (response) {
            console.log(response.context)
            loadValue.innerText = response.context + "/5"
        }
            })
    },1000)
}



window.addEventListener("load", function () {
    if (window.location.pathname === '/dashboard/') {

        let booksLen = document.getElementById("booksLen").value;  // takes number of positions
        for (let comp = 1; comp < booksLen; comp++) {
            let bookAddButton = document.getElementById(`add-btn-${comp}`)
            let bookAddComp = document.getElementById(`add-comp-${comp}`)
            bookAddButton.addEventListener('click', () => {
                if (bookAddComp.classList.contains('d-none') === false) {
                    bookAddComp.classList.toggle('d-none')
                } else {

                    // disable all previously opened submit forms and error msg
                    for (let compDisable = 1; compDisable < booksLen; compDisable++) {
                        let bookAddCompDisable = document.getElementById(`add-comp-${compDisable}`)
                        let errMsgDisable = document.getElementById(`err-msg-${comp}`)
                        if (bookAddCompDisable.classList.contains('d-none') === false) {
                            bookAddCompDisable.classList.toggle('d-none')
                        }
                        if (errMsgDisable.classList.contains('d-none') === false) {
                            errMsgDisable.classList.toggle(('d-none'))
                        }
                    }
                    // open only one submit form at a time
                    bookAddComp.classList.toggle('d-none')
                }

            })

            let submitButton = document.getElementById(`submit-button-${comp}`)

            // show error msg
            submitButton.addEventListener('click', e => {
                let bookInput = document.getElementById(`input-${comp}`).value
                let errMsg = document.getElementById(`err-msg-${comp}`)
                if (bookInput === "") {
                    errMsg.classList.remove('d-none')
                    e.preventDefault()
                }
            })
        }
    }


    if (window.location.pathname === '/collection/mylibrary') {
        let newBookFormButton = document.getElementById('new_book_form_button')
        let newBookForm = document.getElementById('new_book_form')
        let alertMsg = document.getElementById('err-msg')

        // show new book input form
        newBookFormButton.addEventListener('click', () => {
            newBookForm.classList.toggle('d-none')

            // clears alerts while hiding input form
            if (alertMsg.classList.contains('d-none') === false) {
                alertMsg.classList.add('d-none')
            }
        })


        let submitButton = document.getElementById('new-book-submit-form')

        submitButton.addEventListener('click', e => {
            let titleInput = document.getElementById('input-title').value
            let authorInput = document.getElementById('input-author').value
            let dateInput = document.getElementById('input-date').value

            let titleAlert = document.getElementById('err-title')
            let authorAlert = document.getElementById('err-author')
            let dateAlert = document.getElementById('err-date')

            // clears alerts after new submit
            if (titleAlert.classList.contains('d-none') === false) {
                titleAlert.classList.add('d-none')
            }
            if (authorAlert.classList.contains('d-none') === false) {
                authorAlert.classList.add('d-none')
            }
            if (dateAlert.classList.contains('d-none') === false) {
                dateAlert.classList.add('d-none')
            }

            // shows proper alert after invalid submit
            if (titleInput === "" || authorInput === "" || dateInput === "") {
                alertMsg.classList.remove('d-none')
                if (titleInput === "") {
                    titleAlert.classList.remove('d-none')
                }
                if (authorInput === "") {
                    authorAlert.classList.remove('d-none')
                }
                if (dateInput === "") {
                    dateAlert.classList.remove('d-none')
                }
                e.preventDefault()
            }
        })
    }
})
