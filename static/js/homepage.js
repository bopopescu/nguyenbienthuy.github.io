function openSite(urlsite) {
    if (navigator.userAgent.indexOf("Firefox") > 0) {
        window.open( urlsite.toString(), 'newwindow', 'fullscreen,scrollbars');
    }
    else
    {
        window.open( urlsite.toString(), 'newwindow', 'height=' + screen.height + ', width=' + screen.width);
    }
    return false;
}