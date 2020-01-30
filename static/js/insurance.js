$(document).ready(function(e) {
    /*
    $('#add_insurance').keydown(function(e){
        if (e.which === 13) {
            $('#add_insurance').submit();
        }
    });
     */
    let wrapper = $(".table");
    let count_insurance = $(".insurance_code").length;
    //Ẩn nút Remove nếu chỉ có 1 dòng
    $("#count_insurance").val(count_insurance);
    if (count_insurance === 1) {
        $('.del_insurance').hide();
    }
    $(wrapper).on("click", ".add_insurance", function(e) {
        e.preventDefault();
        count_insurance++;
        $("#count_insurance").val(count_insurance);
        let newRowHTML = '<tr>'
            + '<td><button class="btn btn-primary btn-sm add_insurance" tabindex="-1"><i class="fas fa-plus"></i></button> '
            + '<button class="btn btn-danger btn-sm del_insurance" tabindex="-1"><i class="fas fa-minus"></i></button></td>'
            + '<td><input class="form-control insurance insurance_code" name="insurance_code' + count_insurance
            + '" id="insurance_code' + count_insurance + '" type="text" placeholder="Tự động" readonly></td>'
            + '<td><input class="form-control insurance social_company" name="social_company' + count_insurance
            + '" id="social_company' + count_insurance + '" type="text" placeholder="%"></td>'
            + '<td><input class="form-control insurance social_employee" name="social_employee' + count_insurance
            + '" id="social_employee' + count_insurance + '" type="text" placeholder="%"></td>'
            + '<td><input class="form-control insurance health_company" name="health_company' + count_insurance
            + '" id="health_company' + count_insurance + '" type="text" placeholder="%"></td>'
            + '<td><input class="form-control insurance health_employee" name="health_employee' + count_insurance
            + '" id="health_employee' + count_insurance + '" type="text" placeholder="%"></td>'
            + '<td><input class="form-control insurance unemployment_company" name="unemployment_company'
            + count_insurance + '" id="unemployment_company' + count_insurance + '" type="text" placeholder="%"></td>'
            + '<td><input class="form-control insurance unemployment_employee" name="unemployment_employee'
            + count_insurance + '" id="unemployment_employee' + count_insurance + '" type="text" placeholder="%"></td>'
            + '<td><input class="form-control date startday" name="startday' + count_insurance + '" id="startday'
            + count_insurance + '" type="date"></td>'
            + '<td><input class="form-control date endday" name="endday' + count_insurance + '" id="endday'
            + count_insurance + '" type="date"></td>'
            + '<td><input class="form-control insurance designation" name="designation' + count_insurance
            + '" id="designation' + count_insurance + '" type="text" placeholder="Theo quyết định số"></td>'
            + '</tr>';
        $(this).parent().parent().after(newRowHTML);
        //let indexRow = this.parentNode.parentNode.rowIndex;
        //updateIndexElement('main_table', 'emp_email', 'emp_email', 'emp_email', indexRow, 0, "Email ", 0);

        //Nhiều hơn 1 số điện thoại thì show button del_phone ở dòng đầu
        $('.del_insurance').show();
    });
    $(wrapper).on("click", ".del_insurance", function(e) {
        e.preventDefault();
        let indexRow = this.parentNode.parentNode.rowIndex;
        //updateIndexElement('main_table', 'address', 'address', 'address', indexRow, 0, "Địa chỉ ", -1);
        $(this).closest('tr').remove();
        count_insurance--;
        $("#count_insurance").val(count_insurance);
        if (count_insurance === 1) {
            $('.del_insurance').hide();
        }
    });
});

function updateIndexElement(tablename, classname, idname, name, indexRow, indexCol, label, add_rem){
    // add_rem = 0(add) | -1(remove)
    let f = 0;
    //Lấy tất cả element của class address bao gồm cả element mới thêm
     let mem =$('.' + classname);
    let cellRowIndex = $('#' + tablename).find('tr:eq('+ indexRow + ')').find('td:eq(' + indexCol + ')').text();

    let rowUpdateElement = Number(cellRowIndex.replace(label,""))+1;
    let j = 1;
    for (let i=rowUpdateElement, f=mem.length; i<=f; i++) {
        $('#' + tablename).find('tr:eq('+(indexRow+j)+')').find('td:eq(' + indexCol + ')').html(label + (i+add_rem));
        j++;            
    }
    if (add_rem === 0){
        //updateIndexElement (name & id) khi thêm mới
        $('#' + idname + mem.length).attr({'id': idname, 'name': name});
        for (let i=mem.length-1 , f=rowUpdateElement; i>=f; i--) {
            $('#' + idname + i).attr({'id': idname + (i + 1), 'name': name +(i + 1)});            
        }
        $('#' + idname).attr({'id': idname + rowUpdateElement, 'name': name + rowUpdateElement});
    } 
    else {
        //updateIndexElement (name & id) khi xóa 1 phần tử
        for (let i=rowUpdateElement, f=mem.length; i<=f; i++) {
            $('#' + idname + i).attr({'id': idname + (i-1), 'name': name + (i-1)});            
        }
    }
    $('a').click( function(e) {
        e.preventDefault();
        /*your_code_here;*/ 
        window.scrollTo(0,0);
        return false; 
    });
}

