$(document).ready(function(e) {
    $('.dropdown-menu a.dropdown-toggle').on('click', function(e) {
        if (!$(this).next().hasClass('show')) {
            $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
        }
        let $subMenu = $(this).next(".dropdown-menu");
        $subMenu.toggleClass('show');
        $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
            $('.dropdown-submenu .show').removeClass("show");
        });
        return false;
    });
});

function editCompany(){
    //$('#text_change').val("save");
    //document.getElementById('text_changed').innerText = "company_edit";
    //alert(document.getElementById('text_changed').innerText);
    localStorage.frm_actions_company = "COMPANY_EDIT";
}
function changeCompany(){
    //gán nhãn cho frm_actions là điều chỉnh
    localStorage.frm_actions_company = "COMPANY_CHANGE";
}