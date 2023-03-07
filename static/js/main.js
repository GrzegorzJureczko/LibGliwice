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


        // let bookSegment = document.getElementById(`book_segment_${comp}`)
        // let submitButton = document.getElementById(`submit_button_${comp}`)
        // let addInfo = document.getElementById(`add-info_${comp}`)
        //
        // submitButton.addEventListener('click', () => {
        //     bookSegment.classList.add('d-none')
        //     bookAddComp.classList.toggle('d-none')
        //     addInfo.classList.toggle('d-none')
        // })
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
