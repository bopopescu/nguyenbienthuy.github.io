$(document).ready(function(e) {
    $("#salary_basic_amount").keypress(function (e){
        let charCode = (e.which) ? e.which : e.keyCode;
        if ((charCode > 31 && (charCode < 46 || charCode > 57)) || charCode === 47) {
            return false;
        }
    });

    let salary = $(".salary_benefit");

    salary.keypress(function (e){
        let charCode = (e.which) ? e.which : e.keyCode;
        if ((charCode > 31 && (charCode < 46 || charCode > 57)) || charCode === 47) {
            return false;
        }
    });

    salary.focus(function() {
        let s = this.value;
        $('#' + this.id).val(s.replace(/,/g, ""));
        //$("#count_account_number").val(count_account_number);
        //alert(this.id + " | " + this.value);
        //alert(s.replace(/,/g, ""));
    });

    salary.blur(function() {
        let n = parseFloat(this.value);
        $('#' + this.id).val(n.toLocaleString("en-US", { minimumFractionDigits: 2 }));
        //alert(n.toLocaleString("en-US", { minimumFractionDigits: 2 }));
    });

});

function blurSalaryBasicAmount() {
    let n = parseFloat(document.getElementById('salary_basic_amount').value);
    document.getElementById('salary_basic_amount').value =
        n.toLocaleString("en-US", { minimumFractionDigits: 2 });
}

function focusSalaryBasicAmount() {
    let s = document.getElementById('salary_basic_amount').value;
    document.getElementById('salary_basic_amount').value = s.replace(/,/g, "");
}

