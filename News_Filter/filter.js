var comment_list = document.querySelectorAll('#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_favorite > div.u_cbox_content_wrap > ul > li');

for (var i = 0; i < comment_list.length; i++) {
    var comment = comment_list[i].querySelector('div.u_cbox_comment_box > div > div.u_cbox_text_wrap > span.u_cbox_contents')

    if (comment != null) {
        console.log(comment.innerHTML);
        if (i % 5 == 0) {
            comment.innerHTML = '==================== 착한생각 ====================';
        };
    };
};