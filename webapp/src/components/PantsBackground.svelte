<script>
    const aside_img_url = "/resources/Fotografias/Corde-164-original.webp";
</script>


<main  id="cordelia-pants-form" class="page-container">
    <section id="cpf-signup-form-wrapper">
        <slot name="form">Some form</slot>
    </section>
    <section id="aside-pants-image-container">
        <div id="cpf-apic-image-wrapper">
            <img src="{aside_img_url}" alt="pantalones de cordelia" >
        </div>
    </section>
</main>

<style>
    /* DEBUG */
    /* * {
        border: 1px solid red;
    } */

    #cordelia-pants-form {
        --login-page-content-height: calc(100vh - var(--navbar-height));
        --login-page-gradient: linear-gradient(270deg, #f2f1efb7 0%, #F2F1EF 100%) 0% 0% no-repeat padding-box;

        display: grid;
        grid-template-columns: repeat(13, 1fr);
        grid-template-rows: repeat(13, 1fr);
        min-height: var(--login-page-content-height);
        background: var(--login-page-gradient);
    }

    #cpf-signup-form-wrapper {
        display: grid;
        grid-column-start: 1;
        grid-column-end: 8;
        grid-row-start: 1;
        grid-row-end: 14;
        place-items: center;
        background: var(--login-page-gradient);
        z-index: 3;
    }

    #aside-pants-image-container {
        width: 100%;
        grid-area: 1 / 4 / 14 / 14;
        transform: rotateY(180deg);
        z-index: 1;
    }

    @media only screen and (max-width: 768px) {
        #cordelia-pants-form {
            min-height: calc(var(--login-page-content-height) * 1);
        }

        #aside-pants-image-container {
            grid-area: 1 / 1 / 5 / 14 ;
        }

        #aside-pants-image-container img {
            width: 100%;
            max-width: 100%;
        }

        #cpf-signup-form-wrapper {
            grid-column-start: 1;
            grid-column-end: 14;
            grid-row-start: 5;
            grid-row-end: 14;

            place-items: start center;
            padding: var(--spacing-4) 0;
        }        
    }
</style>

