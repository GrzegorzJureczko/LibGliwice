for (let comp = 1; comp < 100; comp++) {
    let bookAddButton = document.getElementById(`add_btn_${comp}`)
    let bookAddComp = document.getElementById(`add_comp_${comp}`)
    bookAddButton.addEventListener('click', () => {
        bookAddComp.classList.toggle('d-none')
    })
}


