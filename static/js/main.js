
$(document).ready(function () {
    function isUniqueId() {
        $('[id]').each(function () {
            var ids = $('[id="' + this.id + '"]');
            if (ids.length > 1 && ids[0] == this)
                console.warn('Multiple IDs #' + this.id);
        });
    }
    isUniqueId();

    $(window).scroll(function () {
        if ($('#header-index').length > 0) {
            if ($(this).scrollTop() > 0) {
                $('#header-index').addClass('header-fix')
            } else {
                $('#header-index').removeClass('header-fix')

            }
        }
    })
    function checkSvg() {
        if ($('.section-menu-user-img').length > 0) {
            ($('.section-menu-user-img').children('img').attr('src').indexOf('svg') != -1)
                ? ($('.section-menu-user-img').css({
                    'overflow': 'visible'
                }))
                : ($('.section-menu-user-img').css({
                    'overflow': 'hidden'
                }))
        }
    }
    checkSvg();

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function getImgName() {
        var filename;
        $('#addUserImg').change(function () {
            var formData = new FormData();

            var csrftoken = getCookie('csrftoken');

            formData.append('file', $('input[type=file]')[0].files[0]);

            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });


            $.ajax({

                url : './change-profile-pic',
                type : 'POST',
                data : formData,
                processData : false,
                contentType : false,
                success : function(data) {

                    data = JSON.parse(data);

                    if (data['key'] == '0') {
                        alert(data['msg']);
                    } else {
                        window.location.reload(true);
                    }

                    // alert(data);
                }

            })
            checkSvg();
        });
    }
    getImgName();
});