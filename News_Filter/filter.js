var comment_list = document.querySelectorAll('#cbox_module > div > div.u_cbox_content_wrap > ul > li');

for (var i = 0; i < comment_list.length; i++) {
    var comment = comment_list[i].querySelector('div.u_cbox_comment_box > div > div.u_cbox_text_wrap > span.u_cbox_contents')

    if (comment != null) {
        if (i % 5 == 0) {
            comment.innerHTML = '◈ 뉴스필터에 의해 가려진 댓글입니다.';
            comment.style.color = "#999";
        };
    };
};