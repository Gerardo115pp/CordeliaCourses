<script>
    import FieldData, { verifyFormFields } from '../../libs/FieldData';
    import { SignUpRequest } from '../../libs/HttpRequests';
    import Input from '../../components/Input.svelte';
    import { push, link } from 'svelte-spa-router';
    import CordeliaPants from '../../components/PantsBackground.svelte';

    const signup_request = new SignUpRequest();
    let is_form_ready = false;

    const form_data = [
        new FieldData('customer_name', /^[A-z\d\s]*$/, 'Nombre'),
        new FieldData('customer_email', /[^;\'\s\n]/, 'Correo electronico', 'email'),
        new FieldData('customer_password', /[^;\s\n]/, 'Contrasena', 'password')
    ]

    // Link FormData to login_request
        $: signup_request.name = form_data[0].getFieldValue();
        $: signup_request.email = form_data[1].getFieldValue();
        $: signup_request.password = form_data[2].getFieldValue();
    // 

    const verifyLoginForm = () => {
        let is_valid = verifyFormFields(form_data);
        is_form_ready = is_valid;
        form_data = [...form_data];
    }

    const signup = () => {
        if (is_form_ready) {
            signup_request.do();
        }
    }

    const aside_img_url = "/resources/Fotografias/Corde-164-original.webp";
</script>

<CordeliaPants>
    <div slot="form" id="clp-signup-form">
        <h2 class="page-title">¡bienvenida!<br/>Crea una cuenta</h2>
        <div id="clp-sf-fields-container">
            {#each form_data as field}
                <div class="clp-sf-fc-field-wrapper">
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
        <div id="clp-sf-form-controls">
            <button id="clp-sf-login-btn" class="full-btn">Crear cuenta</button>
            <button on:click={() => push("/signup")} id="clp-sf-google-btn" class="full-btn">Registrate con google</button>
            <div id="clp-sf-forgot-password">
                <p>¿Ya tienes una? <a href="/login" use:link>Inicia sesion</a></p>
            </div>
        </div>
    </div>
</CordeliaPants>

<style>
    /* DEBUG */
    /* * {
        border: 1px solid red;
    } */


    #clp-signup-form {
        width: 75%;
    }

    #clp-sf-fields-container .clp-sf-fc-field-wrapper{
        margin: var(--spacing-h3) 0;
    }

    #clp-sf-form-controls {
        display: grid;
        height: 20%;
        grid-template: repeat(2, 1fr) / repeat(2, 1fr);
        gap: var(--spacing-3) var(--spacing-3);
    }

    #clp-sf-forgot-password {
        font-weight: lighter;
    }

    #clp-sf-forgot-password a {
        text-transform: capitalize;
    }
    
</style>

