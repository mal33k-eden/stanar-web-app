bus={
    init:()=>{
        $('.cus_submit').click(()=>{
            bus.submitForm()
        })
    },
    submitForm:()=>{
        bp();
        if($('#bus-form')[0].checkValidity()){
            setTimeout(()=>{
                console.log('submitted');
            },3000)
        }else{
            notifyError('Error','Kindly fill out the form correctly');
            setTimeout(()=>{
                $.unblockUI()
            },3000)
        }
        
        
    }

}
$(()=>{
    bus.init()
});