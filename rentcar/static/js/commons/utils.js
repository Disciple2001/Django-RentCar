function showDeleteToast(){
        const t=$(`<div class="toast align-items-center text-white bg-primary border-0" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="d-flex">
    <div class="toast-body">
      Elemento borrado
    </div>
    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
  </div>
</div>`)
        $('#toastarea').append(t)
        const toast =bootstrap.Toast.getOrCreateInstance(t)
        toast.show()
    }
    function showCreateToast(){
        const t=$(`<div class="toast align-items-center text-white bg-primary border-0" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="d-flex">
    <div class="toast-body">
      Elemento creado
    </div>
    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
  </div>
</div>`)
        $('#toastarea').append(t)
        const toast =bootstrap.Toast.getOrCreateInstance(t)
        toast.show()
    }

    function csrf_token(){
        return $('meta[name="csrf_token"]').attr('content')
    }