$(document).ready(function(e) {
    let frm = $('#add_company');
    frm.keydown(function(e){
        if (e.which === 13) {
            //frm.submit();
            $('#save').click();
        }
    });

    $('#form-header').keydown(function(e){
        if (e.which === 13) {
            //frm.submit();
            $('#new_comp').click();
        }
    });

    $('#print').click(function () {
        //let s = $('#add_item');
        //alert($("#company_name").val());
    });
    //Save
    $('#save').click(function () {
        // Cập nhật #flag_test = "save" để lưu data
        $('#flag_test').val("save");
        $('#text_changed').val(localStorage.frm_actions_company);
        frm.submit();
    });
    // Save thử
    $('#test_save').click(function () {
        // Cập nhật #flag_test = "try"
        //alert($("#flag_test").val());
        $('#flag_test').val("try");
        // Load form
        $('#text_changed').val(localStorage.frm_actions_company);
        frm.submit();
    });

    // Kiểm tra nhãn của trang comp_actions.html
    $('#test_local').click(function () {

        alert(localStorage.frm_actions_company);
    });
    $('#update').click(function () {
        let company_id = $('#company_id');
        // Cập nhật #flag_test = "update"
        //alert($("#flag_test").val());
        $('#flag_test').val("update");
        $('#auto_company_id').prop('disabled', true);
        company_id.prop('readonly', false);
        company_id.focus();
        // Load form
        //frm.submit();
    });

    $('#company_id').blur(function () {
        // Load form
        frm.submit();
    });

    $('#reset').click(function () {
        frm.reset();
    });

    //Sự kiện khi tạo mã công ty bằng tay
    $('input[type="checkbox"]').click(function () {
        let company_id = $('#company_id');
        let auto_company_id = $('#auto_company_id');

        if(auto_company_id.prop("checked") === true){
            //'#company_id' chuyển sang readonly
            company_id.prop('readonly', true);
            company_id.val("");
            //alert("Checkbox is checked.");
        }
        else if(auto_company_id.prop("checked") === false){
            company_id.prop('readonly', false);
            company_id.focus();
            //alert("Checkbox is unchecked.");
        }
    });

    // Kiểm tra input có thay đổi hay ko
    $(document).ready(function(){
        $("input").change(function(){
            //alert("The text has been changed.");
            //$('text_changed').val('text_unchanged');
        });
    });
});

/*
function titleCase(str) {
    return str.toLowerCase().replace(/(^|\s)\S/g, function (l) {
       return l.toUpperCase();
    });
}
*/
