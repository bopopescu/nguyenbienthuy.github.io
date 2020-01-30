$(document).ready(function(e) {
    let frm = $('#dept_new');

    // Sự kiện bấm Enter
    frm.keydown(function(e){
        if (e.which === 13) {
            //frm.submit();
            $('#save').click();
        }
    });
    //Save
    $('#save').click(function () {
        // Cập nhật #flag_test = "0" để lưu data
        $('#flag_test').val("0");
        frm.submit();
    });
    // Save thử
    $('#test_save').click(function () {
        // Cập nhật #flag_test = "1"
        //alert($("#flag_test").val());
        $('#flag_test').val("1");
        // Load form
        frm.submit();
    });

    let wrapper = $(".main_table");
    let tb = $("#main_table");
    let count_dept_name = $(".dept_name").length;
    let count_subdept_name = $(".subdept_name").length;

    //Ẩn nút Remove nếu chỉ có 1 dòng
    $("#count_dept_name").val(count_dept_name);
    if (count_dept_name === 1) {
        $('.del_dept_name').hide();
    }
    $("#count_subdept_name").val(count_subdept_name);
    if (count_subdept_name === 1) {
        $('.del_subdept_name').hide();
    }

    $(wrapper).on("click", ".add_dept_name", function(e) {
        e.preventDefault();
        count_dept_name++;
        $("#count_dept_name").val(count_dept_name);
        let indexRow = this.parentNode.parentNode.rowIndex;
        let table = document.getElementById("main_table");
        
        table.insertRow(indexRow+3).innerHTML= "<td>Tên phòng ban " + count_dept_name  + "</td>"
            + "<td><button class=\"btn btn-primary btn-sm add_dept_name\" tabindex=\"-1\"><i class=\"fas fa-plus\"></i></button> "
            + "<button class=\"btn btn-danger btn-sm del_dept_name\" tabindex=\"-1\"><i class=\"fas fa-minus\"></i></button></td>"
            + "<td><input class=\"input-sm form-control-sm form-control dept_name\" type=\"text\" name=\"dept_name" + count_dept_name
            + "\" id=\"dept_name" + count_dept_name + "\" required/></td>";
        table.insertRow(indexRow+4).innerHTML="<td>Từ ngày</td><td></td>"
            + "<td><input class=\"input-sm form-control-sm form-control date startday\" name=\"startday" + count_dept_name
            + "\" id=\"startday" + count_dept_name + "\" type=\"date\" required></td>";
        table.insertRow(indexRow+5).innerHTML="<td>Đến ngày</td><td></td>"
            + "<td><input class=\"input-sm form-control-sm form-control date endday\" name=\"endday" + count_dept_name
            + "\" id=\"endday" + count_dept_name + "\" type=\"date\" value=\"9999-12-31\" disabled></td>";
        
        //Lấy tất cả element của class address bao gồm cả element mới thêm
        let mem =$(".dept_name");
        let cellRowIndex = tb.find('tr:eq('+ indexRow + ')').find('td:eq(' + 0 + ')').text();
        let rowUpdateElement = Number(cellRowIndex.replace("Tên phòng ban ",""))+1;
        let j = 3;
        for (let i=rowUpdateElement, f=mem.length; i<=f; i++) {
            $('#main_table').find('tr:eq('+(indexRow+j)+')').find('td:eq(' + 0 + ')').html('Tên phòng ban ' + i);
            j += 3;            
        }
        //updateIndexElement (name and id)
        $('#dept_name'+ mem.length).attr({'id': 'dept_name', 'name': 'dept_name'});
        $('#startday'+ mem.length).attr({'id': 'startday', 'name': 'startday'});
        $('#endday'+ mem.length).attr({'id': 'endday', 'name': 'endday'});
        for (let i=mem.length-1 , f=rowUpdateElement; i>=f; i--) {
            $('#dept_name'+ i).attr({'id': 'dept_name'+(i+1), 'name': 'dept_name'+(i+1)});
            $('#startday'+ i).attr({'id': 'startday'+(i+1), 'name': 'startday'+(i+1)});
            $('#endday'+ i).attr({'id': 'endday'+(i+1), 'name': 'endday'+(i+1)});
        }
        $('#dept_name').attr({'id': 'dept_name' + rowUpdateElement, 'name': 'dept_name' + rowUpdateElement});
        $('#startday').attr({'id': 'startday' + rowUpdateElement, 'name': 'startday' + rowUpdateElement});
        $('#endday').attr({'id': 'endday' + rowUpdateElement, 'name': 'endday' + rowUpdateElement});

        //$('.dept_name').click(function() {alert(this.id + " | " + this.name);});
        //Nhiều hơn 1 tài khoản thì show button del_dept_name ở dòng đầu
        $('.del_dept_name').show();                       
    });
    
    $(wrapper).on("click", ".del_dept_name", function(e) {
        e.preventDefault();
        let indexRow = this.parentNode.parentNode.rowIndex;
        let mem = $(".dept_name");
        let cellRowIndex = tb.find('tr:eq('+ indexRow + ')').find('td:eq(' + 0 + ')').text();
        let rowUpdateElement = Number(cellRowIndex.replace("Tên phòng ban ","")) + 1;
        let j = 3;// Chỉ cập nhật Label Tên phòng ban 1, 2, 3, ...
        for (let i=rowUpdateElement, f=mem.length; i<=f; i++) {
            $('#main_table').find('tr:eq(' + (indexRow + j) + ')').find('td:eq(' + 0 + ')').html('Tên phòng ban ' + (i-1));
            $('#dept_name' + i).attr({'id': 'dept_name' + (i-1), 'name': 'dept_name' + (i-1)});
            $('#startday' + i).attr({'id': 'startday' + (i-1), 'name': 'startday' + (i-1)});
            $('#endday' + i).attr({'id': 'endday' + (i-1), 'name': 'endday' + (i-1)});  
            j += 3;// Nhảy 3 dòng
        }
        let del_row = $("tr");
        del_row.eq(indexRow+2).remove();// xóa dòng Đến ngày
        del_row.eq(indexRow+1).remove();// xóa dòng Từ ngày
        del_row.eq(indexRow).remove(); // Xóa dòng Tên phòng ban
        count_dept_name--;
        $("#count_dept_name").val(count_dept_name);
        if (count_dept_name === 1) {
            $('.del_dept_name').hide();
        }
    });


    /*
    $('select[name=dept_code]').change(function(){
        let brand_id = $(this).val();
        let request_url = '/sales/get_showrooms/' + brand_id + '/';
        $.ajax({
            url: request_url,
            success: function(data) {
                $.each(data,
                    function (index, text) {
                        $('select[name=showrooms]').append($('<option></option>').val(index).html(text));
                    }
                )
            }
        })
    });
    */
});

