$(document).ready(function(e) {
    let frm = $('#subdept_new');
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
    let count_subdept_name = $(".subdept_name").length;


    $("#count_subdept_name").val(count_subdept_name);
    if (count_subdept_name === 1) {
        $('.del_subdept_name').hide();
    }

    $(wrapper).on("click", ".add_subdept_name", function(e) {
        e.preventDefault();
        count_subdept_name++;
        $("#count_subdept_name").val(count_subdept_name);
        let indexRow = this.parentNode.parentNode.rowIndex;
        let table = document.getElementById("main_table");

        table.insertRow(indexRow+3).innerHTML= "<td>Tên bộ phận " + count_subdept_name  + "</td>"
            + "<td><button class=\"btn btn-primary btn-sm add_subdept_name\" tabindex=\"-1\"><i class=\"fas fa-plus\"></i></button> "
            + "<button class=\"btn btn-danger btn-sm del_subdept_name\" tabindex=\"-1\"><i class=\"fas fa-minus\"></i></button></td>"
            + "<td><input class=\"input-sm form-control-sm form-control subdept_name\" type=\"text\" name=\"subdept_name" + count_subdept_name
            + "\" id=\"subdept_name" + count_subdept_name + "\" placeholder=\"Tên bộ phận\" required/></td>";
        table.insertRow(indexRow+4).innerHTML="<td>Ngày bắt đầu</td><td></td>"
            + "<td><input class=\"input-sm form-control-sm form-control date startday\" name=\"startday" + count_subdept_name
            + "\" id=\"startday" + count_subdept_name + "\" type=\"date\" required></td>";
        table.insertRow(indexRow+5).innerHTML="<td>Ngày kết thúc</td><td></td>"
            + "<td><input class=\"input-sm form-control-sm form-control date endday\" name=\"endday" + count_subdept_name
            + "\" id=\"endday" + count_subdept_name + "\" type=\"date\" value=\"9999-12-31\" disabled></td>";

        //Lấy tất cả element của class address bao gồm cả element mới thêm
        let mem =$(".subdept_name");
        let mt = $('#main_table');
        let cellRowIndex = mt.find('tr:eq('+ indexRow + ')').find('td:eq(' + 0 + ')').text();
        let rowUpdateElement = Number(cellRowIndex.replace("Tên bộ phận ",""))+1;
        let j = 3;
        for (let i=rowUpdateElement, f=mem.length; i<=f; i++) {
            mt.find('tr:eq('+(indexRow+j)+')').find('td:eq(' + 0 + ')').html('Tên bộ phận ' + i);
            j += 3;
        }
        //updateIndexElement (name and id)
        $('#subdept_name'+ mem.length).attr({'id': 'subdept_name', 'name': 'subdept_name'});
        $('#startday'+ mem.length).attr({'id': 'startday', 'name': 'startday'});
        $('#endday'+ mem.length).attr({'id': 'endday', 'name': 'endday'});
        for (let i=mem.length-1 , f=rowUpdateElement; i>=f; i--) {
            $('#subdept_name'+ i).attr({'id': 'subdept_name'+(i+1), 'name': 'subdept_name'+(i+1)});
            $('#startday'+ i).attr({'id': 'startday'+(i+1), 'name': 'startday'+(i+1)});
            $('#endday'+ i).attr({'id': 'endday'+(i+1), 'name': 'endday'+(i+1)});
        }
        $('#subdept_name').attr({'id': 'subdept_name' + rowUpdateElement, 'name': 'subdept_name' + rowUpdateElement});
        $('#startday').attr({'id': 'startday' + rowUpdateElement, 'name': 'startday' + rowUpdateElement});
        $('#endday').attr({'id': 'endday' + rowUpdateElement, 'name': 'endday' + rowUpdateElement});

        //Nhiều hơn 1 tài khoản thì show button del_subdept_name ở dòng đầu
        $('.del_subdept_name').show();
    });

    $(wrapper).on("click", ".del_subdept_name", function(e) {
        e.preventDefault();
        let indexRow = this.parentNode.parentNode.rowIndex;
        let mem = $(".subdept_name");
        let mt = $('#main_table');
        let cellRowIndex = mt.find('tr:eq('+ indexRow + ')').find('td:eq(' + 0 + ')').text();
        let rowUpdateElement = Number(cellRowIndex.replace("Tên bộ phận ","")) + 1;
        let j = 3;// Chỉ cập nhật Label Tên bộ phận 1, 2, 3, ...
        for (let i=rowUpdateElement, f=mem.length; i<=f; i++) {
            mt.find('tr:eq(' + (indexRow + j) + ')').find('td:eq(' + 0 + ')').html('Tên bộ phận ' + (i-1));
            $('#subdept_name' + i).attr({'id': 'subdept_name' + (i-1), 'name': 'subdept_name' + (i-1)});
            $('#startday' + i).attr({'id': 'startday' + (i-1), 'name': 'startday' + (i-1)});
            $('#endday' + i).attr({'id': 'endday' + (i-1), 'name': 'endday' + (i-1)});
            j += 3;// Nhảy 3 dòng
        }
        let row_del = $("tr");
        row_del.eq(indexRow+2).remove();// xóa dòng Ngày kết thúc
        row_del.eq(indexRow+1).remove();// xóa dòng Ngày bắt đầu
        row_del.eq(indexRow).remove(); // Xóa dòng Tên bộ phận
        count_subdept_name--;
        $("#count_subdept_name").val(count_subdept_name);
        if (count_subdept_name === 1) {
            $('.del_subdept_name').hide();
        }
    });

    $('#company').change(function() {
        // get optios of second dropdown and cache it
        let $options = $('#dept').val('').find('option').show();
        // update the dropdown value if necessary
        // get options
        // show all of the initially
        // check current value is not 0
        if (this.value !== null) {
            $options.not('[data-val=\"' + this.value + '\"],[data-val=\"\"]').hide();

            // filter out options which is not corresponds to the first option
            // hide them
        }
    })
});

function titleCase(str) {
    return str.toLowerCase().replace(/(^|\s)\S/g, function (l) {
       return l.toUpperCase();
    });
}

function blurFullname() {
    document.getElementById('fullname').value = titleCase(document.getElementById('fullname').value);
}
