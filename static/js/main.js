if (window.location.pathname === '/dashboard/'){
    let booksLen = document.getElementById("booksLen").value;
    for (let comp = 1; comp < booksLen; comp++) {
    let bookAddButton = document.getElementById(`add_btn_${comp}`)
    let bookAddComp = document.getElementById(`add_comp_${comp}`)
    bookAddButton.addEventListener('click', () => {
           bookAddComp.classList.toggle('d-none')
    })
}
}

if (window.location.pathname === '/collection/mylibrary'){
    let newBookFormButton = document.getElementById('new_book_form_button')
    let newBookForm = document.getElementById('new_book_form')

    newBookFormButton.addEventListener('click', ()=> {
    newBookForm.classList.toggle('d-none')
})

}
