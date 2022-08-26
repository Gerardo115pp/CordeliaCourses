<script>
    import NotificationBubble from '../../components/Notifications/NotificationsBubble.svelte';
    import CordeliaPants from '../../components/PantsBackground.svelte';
    import FieldData, { verifyFormFields } from '../../libs/FieldData';
    import { SignUpRequest } from '../../libs/HttpRequests';
    import Input from '../../components/Input.svelte';
    import { push, link } from 'svelte-spa-router';
import { newNotification } from '../../components/Notifications/events';

    const signup_request = new SignUpRequest();
    let is_form_ready = false;

    let form_data = [
        new FieldData('customer_name', /^[A-z\s]*$/, 'Nombre'),
        new FieldData('customer_email', /[^;\'\s\n]*/, 'Correo electrónico', 'email'),
        new FieldData('customer_password', /[^;\s\n]{8,16}/, 'contraseña', 'password')
    ]

    form_data[0].placeholder = "Nombre Apellido";
    form_data[1].placeholder = "correo con el que hiciste tu compra";
    form_data[2].placeholder = "nueva contraseña";

    // Link FormData to login_request
        let first_name = "";
        let last_name = "";
        $: signup_request.name = first_name;
        $: signup_request.last_name = last_name;
        $: signup_request.email = form_data[1].getFieldValue();
        $: signup_request.password = form_data[2].getFieldValue();
    // 

    const verifySignUpForm = () => {
        let is_valid = verifyFormFields(form_data);
        is_form_ready = is_valid;
        if (is_valid) {
            setNameData(form_data[0].getFieldValue());
        }
        form_data = [...form_data];
    }

    const setNameData = name => {
        const first_space = name.indexOf(" ");
        const names = [name.slice(0, first_space), name.slice(first_space + 1)]
        first_name = names[0];
        last_name = names[1];
    }

    const signup = () => {
        if (is_form_ready) {
            signup_request.do(status_code => {
                if(status_code >= 200 && status_code < 300) {
                    push('/login');
                } else if (status_code === 409) {
                    newNotification("Ya existe una cuenta con este correo");
                } else if (status_code === 406) {
                    newNotification("Por favor, revisa los datos ingresados");
                } else {
                    newNotification(`Error inesperado: ${status_code}`);
                }
            });
        }
    }

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
                        show_placeholder={field.placeholder !== field.name}
                        onEnterPressed={verifySignUpForm}
                        onBlur={verifySignUpForm}
                    />
                </div>
            {/each}
        </div>
        <div id="clp-sf-form-controls">
            <button id="clp-sf-login-btn" on:click={signup} class="full-btn">Crear cuenta</button>
            <button on:click={() => push("/signup")} id="clp-sf-google-btn" class="full-btn">Registrate con google</button>
            <div id="clp-sf-use-login">
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

    #clp-sf-google-btn {
        display: none;
    }

    #clp-sf-use-login {
        grid-area: 2 / 1 / 3 / 2;
        font-weight: lighter;
    }

    #clp-sf-use-login a {
        text-transform: capitalize;
    }

    @media only screen and (max-width: 768px) {
        #clp-sf-form-controls {
            grid-template: auto / repeat(1, 1fr);
        }
    }
    
</style>

