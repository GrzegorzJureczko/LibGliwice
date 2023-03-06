if (window.location.pathname === '/dashboard/') {
    let booksLen = document.getElementById("booksLen").value;  // takes number of positions
    for (let comp = 1; comp < booksLen; comp++) {
        let bookAddButton = document.getElementById(`add_btn_${comp}`)
        let bookAddComp = document.getElementById(`add_comp_${comp}`)
        bookAddButton.addEventListener('click', () => {
            if (bookAddComp.classList.contains('d-none') === false) {
                bookAddComp.classList.toggle('d-none')
            } else {

                // disable all previously opened submit forms and error msg
                for (let compDisable = 1; compDisable < booksLen; compDisable++) {
                    let bookAddCompDisable = document.getElementById(`add_comp_${compDisable}`)
                    let errMsgDisable = document.getElementById(`err_msg_${comp}`)
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

        let submitButton = document.getElementById(`submit_button_${comp}`)

        // show error msg
        submitButton.addEventListener('click', e => {
            let bookInput = document.getElementById(`input_${comp}`).value
            let errMsg = document.getElementById(`err_msg_${comp}`)
            if (bookInput === "") {
                errMsg.classList.toggle('d-none')
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

    newBookFormButton.addEventListener('click', () => {
        newBookForm.classList.toggle('d-none')
    })
}
