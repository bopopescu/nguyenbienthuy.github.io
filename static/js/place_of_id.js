$(document).ready(function(e) {

    $('#add_place_of_id').keydown(function(e){
        if (e.which === 13) {
            $('#add_place_of_id').submit();
        }
    });

    let wrapper = $(".main_table");
    let count_code_place_of_id = $(".code_place_of_id ").length;
    //Ẩn nút Remove nếu chỉ có 1 dòng
    $("#count_code_place_of_id").val(count_code_place_of_id);
    if (count_code_place_of_id === 1) {
        $('.del_place_of_id').hide();
    }
    $(wrapper).on("click", ".add_place_of_id", function(e) {
        e.preventDefault();
        count_code_place_of_id++;
        let indexRow = this.parentNode.parentNode.rowIndex;
        $("#count_code_place_of_id").val(count_code_place_of_id);
        let newRowHTML = '<tr>'
            + '<td>' + count_code_place_of_id + '</td>'
            + '<td><button class="btn btn-primary btn-sm add_place_of_id" tabindex="-1"><i class="fas fa-plus"></i></button> '
            + '<button class="btn btn-danger btn-sm del_place_of_id" tabindex="-1"><i class="fas fa-minus"></i></button></td>'
            + '<td><input class="form-control code_place_of_id" name="code_place_of_id' + count_code_place_of_id
            + '" id="code_place_of_id' + count_code_place_of_id + '" type="text" placeholder="Mã nơi cấp"></td>'
            + '<td><input class="form-control place_of_identification" name="place_of_identification' + count_code_place_of_id
            + '" id="place_of_identification' + count_code_place_of_id + '" type="text" placeholder="Nơi cấp"></td>'
            + '</tr>';
        $(this).parent().parent().after(newRowHTML);
        let mem =$(".code_place_of_id");
        let cellRowIndex = $('#main_table').find('tr:eq('+ indexRow + ')').find('td:eq(' + 0 + ')').text();
        let rowUpdateElement = Number(cellRowIndex)+1;

        let j = 1;
        for (let i=rowUpdateElement, f=mem.length; i<=f; i++) {
            $('#main_table').find('tr:eq('+(indexRow+j)+')').find('td:eq(' + 0 + ')').html(i);
            j++;
        }
        //updateIndexElement (name and id)
        $('#code_place_of_id'+ mem.length).attr({'id': 'code_place_of_id', 'name': 'code_place_of_id'});
        $('#place_of_identification'+ mem.length).attr({'id': 'place_of_identification', 'name': 'place_of_identification'});
        for (let i=mem.length-1 , f=rowUpdateElement; i>=f; i--) {
            $('#code_place_of_id'+ i).attr({'id': 'code_place_of_id'+(i+1), 'name': 'code_place_of_id'+(i+1)});
            $('#place_of_identification'+ i).attr({'id': 'place_of_identification'+(i+1), 'name': 'place_of_identification'+(i+1)});
        }
        $('#code_place_of_id').attr({'id': 'code_place_of_id' + rowUpdateElement, 'name': 'code_place_of_id' + rowUpdateElement});
        $('#place_of_identification').attr({'id': 'place_of_identification' + rowUpdateElement, 'name': 'place_of_identification' + rowUpdateElement});

        //let indexRow = this.parentNode.parentNode.rowIndex;
        //updateIndexElement('main_table', 'emp_email', 'emp_email', 'emp_email', indexRow, 0, "Email ", 0);
        $('.place_of_identification').click(function() { alert(this.id + " | " + this.name);});
        //Nhiều hơn 1 số điện thoại thì show button del_phone ở dòng đầu
        $('.del_place_of_id').show();


    });
    $(wrapper).on("click", ".del_place_of_id", function(e) {
        e.preventDefault();
        //let indexRow = this.parentNode.parentNode.rowIndex;
        //updateIndexElement('main_table', 'address', 'address', 'address', indexRow, 0, "Địa chỉ ", -1);
        $(this).closest('tr').remove();
        count_code_place_of_id--;
        $("#count_code_place_of_id").val(count_code_place_of_id);
        if (count_code_place_of_id === 1) {
            $('.del_place_of_id').hide();
        }
    });
});

