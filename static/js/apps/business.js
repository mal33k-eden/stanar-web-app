let bus={
    
    init:()=>{
        let cs = $('.cus_submit_strict');
        if(cs.length > 0){
            $('.cus_submit_strict').click((e)=>{
                e.preventDefault()
                bus.submitStrictForm()
            })
        }
        $('.upload-logo').click((e)=>{
            e.preventDefault()
            $("input[id='profile_logo']").click()
        })
    },
    submitStrictForm:()=>{
        bp();
        if($('.bus-form')[0].checkValidity()){
            setTimeout(()=>{
                $('.bus-form').closest('form').submit();
            },3000)
        }else{
            notifyError('Error','Kindly fill out the form correctly');
            setTimeout(()=>{
                $.unblockUI()
            },3000)
        }    
    },
    submitForm:(el)=>{
        bp();
        setTimeout(()=>{
            el.closest('form').submit();
        },3000)
    },
    uploadPhoto:()=>{
        //bp();
        console.log('herere')
    }

}
$(()=>{
    bus.init()
});