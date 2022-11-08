function Register(){
    let First_Name = document.getElementById('First_Name').value;
    let Last_Name = document.getElementById('Last_Name').value;
    let Email_Address = document.getElementById('Email_Address').value;
    let User_Name = document.getElementById('User_Name').value;
    let Password = document.getElementById('Password').value;
    let Confirm_Password = document.getElementById('Confirm_Password').value;
    if(First_Name == "")
    {
        Swal.fire({
            icon: 'error',
            title: 'Lỗi',
            text: 'Vui lòng nhập First Name',
          })
    }
}