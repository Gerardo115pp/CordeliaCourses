<script>
import App from '../../App.svelte';

    import FieldData, { verifyFormFields } from '../../libs/FieldData';
    import { LoginRequest } from '../../libs/HttpRequests';
    import Input from '../../components/Input.svelte';

    const login_request = new LoginRequest();
    let is_form_ready = false;

    const form_data = [
        new FieldData('customer_email', /[^;\'\s\n]/, 'Correo electronico', 'email'),
        new FieldData('customer_password', /[^;\s\n]/, 'Contrasena', 'password')
    ]

    // Link FormData to login_request
        $: login_request.email = form_data[0].getFieldValue();
        $: login_request.password = form_data[1].getFieldValue();
    // 

    const verifyLoginForm = () => {
        let is_valid = verifyFormFields(form_data);
        is_form_ready = is_valid;
        form_data = [...form_data];
    }

    const login = () => {
        if (is_form_ready) {
            login_request.do();
        }
    }

    const aside_img_url = "/resources/Fotografias/Corde-164-original.webp";
</script>

<main id="cordelia-login-page" class="page-container">
    <section id="clp-login-form-wrapper">
        <div id="clp-login-form">
            <h2 class="page-title">iniciar sesión</h2>
            <div id="clp-lf-fields-container">
                {#each form_data as field}
                    <div class="clp-lf-fc-field-wrapper">
                        <Input
                            field_data={field}
                            isClear={true}
                            isSquared={true}
                            input_label={field.name}
                            onEnterPressed={verifyLoginForm}
                            onBlur={verifyLoginForm}
                        />
                    </div>
                {/each}
            </div>
            <div id="clp-lf-form-controls">
                <button id="clp-lf-login-btn" class="full-btn">Iniciar sesion</button>
                <button id="clp-lf-google-btn" class="full-btn">Registrate con google</button>
                <div id="clp-lf-remember-user">
                    <div id="clp-lf-ru-input">
                        <input type="checkbox" id="clp-lf-remember-user-checkbox" />
                        <label for="clp-lf-remember-user-checkbox">Recordarme</label>
                    </div>
                </div>
                <div id="clp-lf-forgot-password">
                    <a href="/#">Olvidé mi contraseña</a>
                </div>
            </div>
        </div>
    </section>
    <section id="aside-pants-image-container">
        <div id="clp-apic-image-wrapper">
            <img src="{aside_img_url}" alt="pantalones de cordelia" >
        </div>
    </section>
</main>

<style>
    /* DEBUG */
    /* * {
        border: 1px solid red;
    } */

    #cordelia-login-page {
        --login-page-content-height: calc(100vh - var(--navbar-height));
        --login-page-gradient: linear-gradient(270deg, #f2f1efb7 0%, #F2F1EF 100%) 0% 0% no-repeat padding-box;

        display: grid;
        grid-template-columns: repeat(13, 1fr);
        grid-template-rows: repeat(13, 1fr);
        background: var(--login-page-gradient);
    }

    #clp-login-form-wrapper {
        display: grid;
        grid-column-start: 1;
        grid-column-end: 8;
        grid-row-start: 1;
        grid-row-end: 14;
        place-items: center;
        background: var(--login-page-gradient);
        z-index: 3;
    }

    #clp-login-form {
        width: 75%;
    }

    #clp-lf-fields-container .clp-lf-fc-field-wrapper{
        margin: var(--spacing-h3) 0;
    }

    #aside-pants-image-container {
        width: 100%;
        grid-area: 1 / 4 / 14 / 14;
        transform: rotateY(180deg);
        z-index: 1;
    }

    #clp-lf-form-controls {
        display: grid;
        height: 20%;
        grid-template: repeat(2, 1fr) / repeat(2, 1fr);
        gap: var(--spacing-3) var(--spacing-3);
    }

    #clp-lf-remember-user {
        display: flex;
        justify-content: center;
        align-items: flex-start;
    }

    #clp-lf-ru-input {
        display: flex;
        width: 55%;
        height: 50%;
        justify-content: space-around;
        align-items: center;
    }

    #clp-lf-remember-user label {
        font-family: var(--font-text);
        font-size: var(--font-size-3);
    }

    #clp-lf-forgot-password {
        text-align: right;
        font-weight: lighter;
        padding: 0 var(--spacing-2) 0 0;
    }
    
</style>

