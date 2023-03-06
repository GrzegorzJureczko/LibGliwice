if (window.location.pathname === '/dashboard/') {
    let booksLen = document.getElementById("booksLen").value;  // takes number of positions
    for (let comp = 1; comp < booksLen; comp++) {
        let bookAddButton = document.getElementById(`add_btn_${comp}`)
        let bookAddComp = document.getElementById(`add_comp_${comp}`)
        bookAddButton.addEventListener('click', () => {

            // disable all previously opened submit forms
            for (let compDisable = 1; compDisable < booksLen; compDisable++) {
                let bookAddCompDisable = document.getElementById(`add_comp_${compDisable}`)
                if (bookAddCompDisable.classList.contains('d-none') === false) {
                    bookAddCompDisable.classList.toggle('d-none')
                }
            }
            // open only one submit form at a time
            bookAddComp.classList.toggle('d-none')
        })
    }
}


if (window.location.pathname === '/collection/mylibrary') {
    let newBookFormButton = document.getElementById('new_book_form_button')
    let newBookForm = document.getElementById('new_book_form')

    newBookFormButton.addEventListener('click', () => {
        newBookForm.classList.toggle('d-none')
    })
}
