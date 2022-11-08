(function() {
    $('#DataTable').DataTable({
        paging: true, // Hiển thị số trang lật
        pageLength: 10, // Giới hạn cho mỗi bảng trong trang
        lengthChange: true, // Hiển thị giới hạn cho mỗi bảng
        autoWidth: true, // Tự động căn chỉnh
        searching: true, // Hiển thị Search
        bInfo: false, //Hiển thị số cột trong bảng
        bSort: true, //Hiển thị nút nhấn chuyển trang bảng

        "columnDefs":[{
            "targets": [7, 8],
            "orderable": false
        }],

        dom: 'lBfrtip',
        buttons: [
            {
                // COPY
                extend: 'copy',
                text: '<i class = "fas fa-clone"></i>',
                className: 'btn btn-secondary',
                titleAttr: 'Copy',
                exportOptions:{
                    columns: [0, 1, 2, 3, 4, 5, 6, 7]
                }
            },
            {
                // EXEL
                extend: 'excel',
                text: '<i class = "fas fa-file-excel"></i>',
                className: 'btn btn-secondary',
                titleAttr: 'Excel',
                exportOptions:{
                    columns: [0, 1, 2, 3, 4, 5, 6, 7]
                }
            },
            {
                // PRINT
                extend: 'print',
                text: '<i class = "fas fa-print"></i>',
                className: 'btn btn-secondary',
                titleAttr: 'Print',
                exportOptions:{
                    columns: [0, 1, 2, 3, 4, 5, 6, 7]
                },
                // Font SIZE
                customize: function(win){
                    $(win.document.body).css('font-size', '10pt')
                    $(win.document.body).find('table')
                        .addClass('compact')
                        .css('font-size', 'inherit');
                }
            },
            {
                // PDF
                extend: 'pdf',
                text: '<i class = "fas fa-file-pdf"></i>',
                className: 'btn btn-secondary',
                titleAttr: 'PDF',
                exportOptions:{
                    columns: [0, 1, 2, 3, 4, 5, 6, 7]
                },
                // Center TABLE
                tableHeader:{
                    alignment: 'center'
                },
                customize: function(doc){
                    doc.styles.tableHeader.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableHeader.fontSize = 7;
                    doc.defaultStyle.fontSize = 6;
                    doc.content[1].table.widths = Array(doc.content[1].table.body[1].length  + 1).join('*').split('');

                }
            },
        ]
    });
})();