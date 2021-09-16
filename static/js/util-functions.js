
function bp(){
    $.blockUI({message:'<div class="spinner-border text-warning m-1" role="status"><span class="sr-only">Loading...</span></div>'});
}
function notifyError(title,msg){
    let options = {
        "closeButton": false,
        "debug": false,
        "newestOnTop": true,
        "progressBar": true,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": 300,
        "hideDuration": 1000,
        "timeOut": 5000,
        "extendedTimeOut": 1000,
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }
    if(title=='Info'){
        toastr.info(msg,title)
    }
    if(title=='Success'){
        toastr.success(msg,title,options)
    }
    if(title=='Warning'){
        toastr.warning(msg,title,options)
    }
    if(title=='Error'){
        toastr.error(msg,title,options)
    }
     
}