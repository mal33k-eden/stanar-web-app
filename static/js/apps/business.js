let bus={
    
    init:()=>{
        
        let cs = $('.cus_submit_strict');
        let s2 = $('.select2');
        if(cs.length > 0){
            $('.cus_submit_strict').click((e)=>{
                e.preventDefault()
                bus.submitStrictForm()
            })
        }
        if(s2.length > 0){
            s2.select2();
        }
        $('.upload-logo').click((e)=>{
            e.preventDefault()
            $("input[id='profile_logo']").click()
        })
        $('.upload-banner').click((e)=>{
            e.preventDefault()
            $("input[id='profile_banner']").click()
        })
        $('.upload-display-1').click((e)=>{
            e.preventDefault()
            $("input[id='profile_display_1']").click()
        })
        $('.upload-display-2').click((e)=>{
            e.preventDefault()
            $("input[id='profile_display_2']").click()
        })
        $('.upload-display-3').click((e)=>{
            e.preventDefault()
            $("input[id='profile_display_3']").click()
        })
        $('.upload-display-4').click((e)=>{
            e.preventDefault()
            $("input[id='profile_display_4']").click()
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
    submitSpecificForm:(el,formID)=>{
        bp();
        console.log(formID)
        setTimeout(()=>{
            $("#-"+formID).submit()
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