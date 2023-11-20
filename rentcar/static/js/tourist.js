$(document).ready(async function () {
    const tourist_modal =  bootstrap.Modal.getOrCreateInstance($('#tourist-modal'))

    function cargar_tourist(){
        $('table tbody').load('http://127.0.0.1:8000/tourist/list',function () {

            configurar_delete()
            configurar_detalles()
        })
    }

    function configurar_delete() {
        $('button.btn-delete').click(function (e) {
            e.preventDefault();
            const btn = $(this);
            $.post(btn.data('delete-url'),{
                csrfmiddlewaretoken:csrf_token()
            },function (){
                showDeleteToast();
                btn.parents('tr').remove()
            })
        })
    }

    function configurar_detalles(){
        $('button.btn-detail').click(function (e) {
            e.preventDefault();
            const btn = $(this);
            $.get(btn.data('detail-url'),function (data, status){
                const modal = $(data)
                $('body').append(modal)
                bootstrap.Modal.getOrCreateInstance(modal).show()
            })
        })
    }
    function configurar_crear(){
        $('#btn-crear').click(function(){
            $('.modal-dialog').load('http://127.0.0.1:8000/tourist/create',function () {
                tourist_modal.show()
                $('input[name="birth_date"]').attr('type','date')

                function form_event (e) {
                    e.preventDefault()
                    const params = Object.create({})
                    $(this).find('input').each(( index, element)=>{
                        const i = $( element )
                        console.log(i)
                        params[i.attr('name')] = i.val()
                    })
                    console.log(params)
                    $.ajax({
                        type:     "post",
                        data:     params,
                        url:      'http://127.0.0.1:8000/tourist/create',
                        error: function (request, error) {
                            $('.modal-dialog').html(request.responseText)
                            $('#tourist-form').submit(form_event);
                            console.log(arguments);
                        },
                        success: function (data) {
                            tourist_modal.hide()
                            showCreateToast()
                            cargar_tourist()

                        }
                    })
                }
                $('#tourist-form').submit(form_event);
            })

        })
    }
    configurar_crear()
    cargar_tourist()
})