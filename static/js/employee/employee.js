$(document).ready(function() {
    let frmmain = $('.employee_new');
    let fullname = $('.fullname');
    let company = $('.company');
    let dept = $('.dept');
    let subdept = $('.subdept');
    let gender = $('.gender');
    let idname = $('.idname');
    let idplace = $('.place_of_identification');
    let people = $('.people');
    let country = $('.nation');



    $('frmmain').keydown(function(e){
        if (e.which === 13) {
            //$('#employee_new').submit();
        }
    });                 
    let wrapper = $(".card-body");
    let count_address = $(".address").length;
    let count_phone = $(".phone_number").length;
    let count_email = $(".emp_email").length;
    let count_account_number = $(".account_number").length;

    //Ẩn nút Remove nếu chỉ có 1 dòng
    $("#count_address").val(count_address);
    if (count_address === 1) {
        $('.del_address').hide();
    }

    $("#count_phone").val(count_phone);
    if (count_phone === 1) {
        $('.del_phone').hide();
    } 

    $("#count_email").val(count_email);
    if (count_email === 1) {
        $('.del_email').hide();
    } 

    $("#count_account_number").val(count_account_number);
    if (count_account_number === 1) {
        $('.del_account_number').hide();
    }

    // Xóa địa chỉ
    $(wrapper).on("click", ".del_address", function(e) {
        e.preventDefault();
        // Vị trí xóa
        let indexrow = getIndex($(this).parent().parent().children().children().attr("for"),"address");
        //Xóa dòng
        $(this).closest('div').parent().remove();
        count_address--;
        if (count_address === 1) {
            $('.del_address').hide();
        }
        //Cập nhật nhãn
        updateIndexElement(indexrow, count_address + 1,
            'address', 'address', 'Địa chỉ ', -1);
        $("#count_address").val(count_address);
    });
    //Thêm địa chỉ
    $(wrapper).on("click", ".add_address", function(e) {
        e.preventDefault();
        count_address++;
        // cập nhật số lượng địa chỉ
        $("#count_address").val(count_address);
        // thêm dòng
        let newRowHTML = '<div class="row">'
            + '<div class="col col-sm-2">'
            + '<label for="address' + count_address + '" class="form-control-sm">Địa chỉ ' + count_address + '</label>'
            + '</div>'
            + '<div class="col col-sm-1">'
            + '<button class="btn btn-primary btn-sm add_address" tabindex="-1"><i class="fas fa-plus"></i></button> '
            + '<button class="btn btn-danger btn-sm del_address" tabindex="-1"><i class="fas fa-minus"></i></button>'
            + '</div>'
            + '<div class="col-6 col-sm-4">'
            + '<input class="input-sm form-control-sm form-control address" type="text" name="address' + count_address
            + '" id="address' + count_address + '" required/>'
            + '</div>'
            + '</div>';
        $(this).parent().parent().after(newRowHTML);
        // Vị trí insert dòng mới
        let indexrow = getIndex($(this).parent().parent().children().children().attr("for"),"address") + 1;
        // Cập nhật label, id, name
        updateIndexElement(indexrow, count_address,
            'address', 'address', 'Địa chỉ ', 1);
        //Nhiều hơn 1 địa chỉ thì show button del_address ở dòng đầu
        $('.del_address').show();
    });
    // Thêm số điện thoại
    $(wrapper).on("click", ".add_phone", function(e) {
        e.preventDefault();
        count_phone++;
        $("#count_phone").val(count_phone);
        let newRowHTML = '<div class="row">'
            + '<div class="col col-sm-2">'
            + '<label for="phone_number' + count_phone + '" class="form-control-sm">Số điện thoại ' + count_phone + '</label>'
            + '</div>'
            + '<div class="col col-sm-1">'
            + '<button class="btn btn-primary btn-sm add_phone" tabindex="-1"><i class="fas fa-plus"></i></button> '
            + '<button class="btn btn-danger btn-sm del_phone" tabindex="-1"><i class="fas fa-minus"></i></button>'
            + '</div>'
            + '<div class="col-6 col-sm-2">'
            + '<input class="input-sm form-control-sm form-control phone_number" type="text" name="phone_number' + count_phone
            + '" id="phone_number' + count_phone + '" required/>'
            + '</div>'
            + '</div>';
        $(this).parent().parent().after(newRowHTML);
        // Vị trí insert dòng mới
        let indexrow = getIndex($(this).parent().parent().children().children().attr("for"),"phone_number") + 1;
        // Cập nhật label, id, name
        updateIndexElement( indexrow, count_phone,
            'phone_number', 'phone_number', 'Số điện thoại ', 1);
        //Nhiều hơn 1 số điện thoại thì show button del_phone ở dòng đầu
        $('.del_phone').show();                       
    });
    // Xóa số điện thoại
    $(wrapper).on("click", ".del_phone", function(e) {
        e.preventDefault();
        let txtLabel = 'Số điện thoại ';// label có khoảng trống cuối chuỗi
        // Vị trí xóa
        let indexrow = getIndex($(this).parent().parent().children().children().attr("for"),"phone_number");
        $(this).closest('div').parent().remove();
        count_phone--;
        $("#count_phone").val(count_phone);
        if (count_phone === 1) {
            $('.del_phone').hide();
        }
        // Cập nhật nhãn
        updateIndexElement(indexrow,count_phone + 1,
            'phone_number', 'phone_number', txtLabel, -1);
    });
    // Thêm email
    $(wrapper).on("click", ".add_email", function(e) {
        e.preventDefault();
        count_email++;
        $("#count_email").val(count_email);
        let newRowHTML = '<div class="row">'
            + '<div class="col col-sm-2">'
            + '<label for="emp_email' + count_email + '" class="form-control-sm">Email ' + count_email + '</label>'
            + '</div>'
            + '<div class="col col-sm-1">'
            + '<button class="btn btn-primary btn-sm add_email" tabindex="-1"><i class="fas fa-plus"></i></button> '
            + '<button class="btn btn-danger btn-sm del_email" tabindex="-1"><i class="fas fa-minus"></i></button>'
            + '</div>'
            + '<div class="col-6 col-sm-3">'
            + '<input class="input-sm form-control-sm form-control emp_email" type="text" name="emp_email' + count_email
            + '" id="emp_email' + count_email + '" required/>'
            + '</div>'
            + '</div>';
        $(this).parent().parent().after(newRowHTML);
        // Vị trí insert dòng mới
        let indexrow = getIndex($(this).parent().parent().children().children().attr("for"),"emp_email") + 1;
        // Cập nhật label, id, name
        updateIndexElement(indexrow, count_email,
            'emp_email', 'emp_email',"Email ", 1);
        //Nhiều hơn 1 số điện thoại thì show button del_phone ở dòng đầu
        $('.del_email').show();                       
    });
    // Xóa email
    $(wrapper).on("click", ".del_email", function(e) {
        e.preventDefault();
        // Vị trí xóa
        let indexrow = getIndex($(this).parent().parent().children().children().attr("for"),"emp_email");
        $(this).closest('div').parent().remove();
        count_email--;
        $("#count_email").val(count_email);
        if (count_email === 1) {
            $('.del_email').hide();
        }
        // Cập nhật nhãn
        updateIndexElement(indexrow,count_email + 1,
            'emp_email', 'emp_email', "Email ", -1);
    });
    // Thêm số tài khoản ngân hàng
    $(wrapper).on("click", ".add_account_number", function(e) {
        e.preventDefault();
        count_account_number++;
        $("#count_account_number").val(count_account_number);
        // Vị trí insert dòng mới
        let indexrow = getIndex($(this).parent().parent().children().children().attr("for"),"account_number") + 1;
        // Thêm dòng tài khoản ngân hàng
        let newRowHTML = '<div><div class="row">'
            + '<div class="col col-sm-2">'
            + '<label for="account_number' + count_account_number + '" class="form-control-sm">Số tài khoản ' + count_account_number + '</label>'
            + '</div>'
            + '<div class="col col-sm-1">'
            + '<button class="btn btn-primary btn-sm add_account_number" tabindex="-1"><i class="fas fa-plus"></i></button> '
            + '<button class="btn btn-danger btn-sm del_account_number" tabindex="-1"><i class="fas fa-minus"></i></button>'
            + '</div>'
            + '<div class="col-6 col-sm-3">'
            + '<input class="input-sm form-control-sm form-control account_number" type="text" name="account_number' + count_account_number
            + '" id="account_number' + count_account_number + '" required/>'
            + '</div></div>'
            + '<div class="row">'
            + '<div class="col col-sm-2">'
            + '<label for="bank_name' + count_account_number + '" class="form-control-sm">Ngân hàng</label>'
            + '</div>'
            + '<div class="col col-sm-1"></div>'
            + '<div class="col-6 col-sm-4">'
            + '<input class="input-sm form-control-sm form-control bank_name" type="text" name="bank_name' + count_account_number
            + '" id="bank_name' + count_account_number + '" required/>'
            + '</div></div>'
            + '<div class="row">'
            + '<div class="col col-sm-2">'
            + '<label for="bank_address' + count_account_number + '" class="form-control-sm">Địa chỉ ngân hàng</label>'
            + '</div>'
            + '<div class="col col-sm-1"></div>'
            + '<div class="col-6 col-sm-4">'
            + '<input class="input-sm form-control-sm form-control bank_address" type="text" name="bank_address' + count_account_number
            + '" id="bank_address' + count_account_number + '" required/>'
            + '</div></div></div>';
        // Cập nhật sau thẻ div tổng
        $(this).parent().parent().parent().after(newRowHTML);

        //updateIndexElement (for of label, name and id)
        // Số tài khoản
        $('label[for="account_number' + count_account_number + '"]').attr('for', 'account_number');
        $('#account_number'+ count_account_number).attr({'id': 'account_number', 'name': 'account_number'});
        // Mở tại
        $('label[for="bank_name' + count_account_number + '"]').attr('for', 'bank_name');
        $('#bank_name'+ count_account_number).attr({'id': 'bank_name', 'name': 'bank_name'});
        // Địa chỉ nơi mở tk
        $('label[for="bank_address' + count_account_number + '"]').attr('for', 'bank_address');
        $('#bank_address'+ count_account_number).attr({'id': 'bank_address', 'name': 'bank_address'});
        for (let i = count_account_number - 1; i >= indexrow; i--) {
            $('label[for="account_number' + i + '"]').attr('for', 'account_number' + (i + 1));
            $('#account_number' + i).attr({'id': 'account_number' + (i + 1), 'name': 'account_number' + (i + 1)});
            $('label[for="bank_name' + i + '"]').attr('for', 'bank_name' + (i + 1));
            $('#bank_name' + i).attr({'id': 'bank_name' + (i + 1), 'name': 'bank_name' + (i + 1)});
            $('label[for="bank_address' + i + '"]').attr('for', 'bank_address' + (i + 1));
            $('#bank_address' + i).attr({'id': 'bank_address' + (i + 1), 'name': 'bank_address' + (i + 1)});
        }
        $('label[for="account_number"]').attr('for', 'account_number' + indexrow);
        $('#account_number').attr({'id': 'account_number' + indexrow, 'name': 'account_number' + indexrow});
        $('label[for="bank_name"]').attr('for', 'bank_name' + indexrow);
        $('#bank_name').attr({'id': 'bank_name' + indexrow, 'name': 'bank_name' + indexrow});
        $('label[for="bank_address"]').attr('for', 'bank_address' + indexrow);
        $('#bank_address').attr({'id': 'bank_address' + indexrow, 'name': 'bank_address' + indexrow});

        // Cập nhật label Số tài khoản
        for (let i = indexrow; i<=count_account_number; i++){
            document.querySelector("label[for=account_number" + i + "]").textContent = "Số tài khoản " + i;
        }
        //$('.account_number').click(function() {alert(this.id + " | " + this.name);});
        //Nhiều hơn 1 tài khoản thì show button del_account_number ở dòng đầu
        $('.del_account_number').show();                       
    });
    // Xóa số tài khoản ngân hàng
    $(wrapper).on("click", ".del_account_number", function(e) {
        e.preventDefault();
        // Vị trí xóa
        let indexrow = getIndex($(this).parent().parent().children().children().attr("for"),"account_number");
        $(this).closest('div').parent().parent().remove();
        count_account_number--;
        $("#count_account_number").val(count_account_number);
        if (count_account_number === 1) {
            $('.del_account_number').hide();
        }
        //updateIndexElement (for of label, name and id)
        for (let i = indexrow; i <= count_account_number+1; i++) {
            $('label[for="account_number' + i + '"]').attr('for', 'account_number' + (i - 1));
            $('#account_number' + i).attr({'id': 'account_number' + (i - 1), 'name': 'account_number' + (i - 1)});

            $('label[for="bank_name' + i + '"]').attr('for', 'bank_name' + (i - 1));
            $('#bank_name' + i).attr({'id': 'bank_name' + (i - 1), 'name': 'bank_name' + (i - 1)});
            $('label[for="bank_address' + i + '"]').attr('for', 'bank_address' + (i - 1));
            $('#bank_address' + i).attr({'id': 'bank_address' + (i - 1), 'name': 'bank_address' + (i - 1)});
        }
        // Cập nhật label Số tài khoản
        for (let i = indexrow; i <= count_account_number+1; i++) {
            document.querySelector("label[for=account_number" + i + "]").textContent = "Số tài khoản " + i;
        }
    });

    // Proper text
    $(fullname).blur(function() {$(this).val(titleCase($(this).val()));});
    // Fill company like dept
    // Fill company
    $(company).focus(function () {
        let url = $(frmmain).attr("data-companies-url");
        let selected_company = $('#selected_company').val();
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'selected_company': selected_company       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $(company).html(data);  // replace the contents of the city input with the data that came from the server
            }
        });
    }).trigger('focus');
    // Fill company change
    $(company).change(function() {
        let url = $(frmmain).attr("data-depts-url");  // get the url of the `load_cities` view
        let company_id = $(this).val();  // get the selected country ID from the HTML input
        let selected_dept = $("#selected_dept").val();
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'company': company_id,       // add the country id to the GET parameters
                'selected_dept': selected_dept
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $(dept).html(data);  // replace the contents of the city input with the data that came from the server
                let dept_id = $(dept).val(); //when #dept is empty then reset #subdept
                if (dept_id === '') {
                    $(subdept).html('<option value="">Chọn bộ phận...</option>');
                }
            }
        });
    }).trigger('change');
    // Fill dept
    $(dept).focus(function() {
        let url = $(frmmain).attr("data-depts-url");  // get the url of the `load_cities` view
        let company_id = $(company).val();  // get the selected country ID from the HTML input
        let selected_dept = $("#selected_dept").val();
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'company': company_id,       // add the country id to the GET parameters
                'selected_dept': selected_dept
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $(dept).html(data);  // replace the contents of the city input with the data that came from the server
            }
        });
    });
    // Fill dept like subdept
    $(dept).change(function() {
        let url = $(frmmain).attr("data-subdepts-url");  // get the url of the `load_cities` view
        let dept_id = $(this).val();  // get the selected country ID from the HTML input
        let selected_subdept = $("#selected_subdept").val();
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'dept': dept_id,       // add the country id to the GET parameters
                'selected_subdept': selected_subdept,
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $(subdept).html(data);  // replace the contents of the city input with the data that came from the server
            }
        });
    }).trigger("change");
    // Fill subdept
    $(subdept).focus(function() {
        let url = $(frmmain).attr("data-subdepts-url");  // get the url of the `load_cities` view
        let dept_id = $(dept).val();  // get the selected country ID from the HTML input
        let selected_subdept = $("#selected_subdept").val();
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'dept': dept_id,       // add the country id to the GET parameters
                'selected_subdept': selected_subdept,
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $(subdept).html(data);  // replace the contents of the city input with the data that came from the server
            }
        });
    });
    // Fill gender
    $(gender).focus(function () {
        let url = $(frmmain).attr("data-genders-url");
        let selected_gender = $('#selected_gender').val();
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'selected_gender': selected_gender       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $(gender).html(data);  // replace the contents of the city input with the data that came from the server
            }
        });
    }).trigger('focus');
    // Fill idname
    $(idname).focus(function () {
        let url = $(frmmain).attr("data-idnames-url");
        let selected_idname = $('#selected_idname').val();
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'selected_idname': selected_idname       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $(idname).html(data);  // replace the contents of the city input with the data that came from the server
            }
        });
    }).trigger('focus');
    //Fill Nơi cấp CMND/Hộ chiếu
    $(idplace).focus(function () {
        let url = $(frmmain).attr("data-idplaces-url");
        let selected_idplace = $('#selected_idplace').val();
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'selected_idplace': selected_idplace       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $(idplace).html(data);  // replace the contents of the city input with the data that came from the server
            }
        });
    }).trigger('focus');
    //Fill dân tộc
    $(people).focus(function () {
        let url = $(this).attr("data-people-url");
        let selected_people = $('#selected_people').val();
        $.ajax({
            url: url,
            data: {
                'selected_people': selected_people
            },
            success: function (data) {
                $(people).html(data);
            }
        });
    }).trigger('focus');
    //Fill quốc tịch
    $(country).focus(function () {
        let url = $(this).attr("data-countries-url");
        let selected_country = $('#selected_country').val();
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'selected_country': selected_country       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $(country).html(data);  // replace the contents of the city input with the data that came from the server
            }
        });
    }).trigger('focus');


    // Start page then fullname focus
    $(fullname).trigger('focus');

});
//Cập nhật Label, id, name cho input
function updateIndexElement(indexrow, indexrowlast, idname, name, label, add_rem){
    // add_rem = 0(add) | -1(remove)
    if (add_rem === 1) {
        // Cập nhật for of label
        $('label[for="' + name + indexrowlast + '"]').attr('for', name);
        // id, name
        $('#' + idname + indexrowlast).attr({'id': idname, 'name': name});
        for (let i = indexrowlast - 1; i >= indexrow; i--) {
            $('label[for="' + name + i + '"]').attr('for', name + (i + 1));
            $('#' + idname + i).attr({'id': idname + (i + 1), 'name': 'name' + (i + 1)});
        }
        $('label[for="' + name + '"]').attr('for', name + indexrow);
        $('#' + idname).attr({'id': idname + indexrow, 'name': name + indexrow});
    }
    else{
        if (add_rem === -1) {
            for (let i = indexrow; i <= indexrowlast; i++) {
                $('label[for="' + name + i + '"]').attr('for', name + (i - 1));
                $('#' + idname + i).attr({'id': idname + (i - 1), 'name': name + (i - 1)});
            }
        }
    }
    // Cập nhật label
    for (let i = indexrow; i<=indexrowlast; i++){
        document.querySelector("label[for=" + name + i + "]").textContent = label + i;
    }
}
// In hoa ký tự đầu mỗi chữ
function titleCase(str) {
    return str.toLowerCase().replace(/(^|\s)\S/g, function (l) {
       return l.toUpperCase();
    });
}

// Lấy phần số cuối trong chuỗi
function getIndex(strnum, str_repl) {
    return Number(strnum.replace(str_repl,""));
}
