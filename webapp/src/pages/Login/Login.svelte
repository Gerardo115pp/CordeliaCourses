<script>
    import FieldData, { verifyFormFields } from '../../libs/FieldData';
    import CordeliaPants from '../../components/PantsBackground.svelte';
    import cordelia_storage from '../../libs/local_storage';
    import { LoginRequest } from '../../libs/HttpRequests';
    import Input from '../../components/Input.svelte';
    import { push, link } from 'svelte-spa-router';
    import { onMount } from 'svelte';


    onMount(() => {
        if (cordelia_storage.Token !== "") {
            push('/courses');
        }
    });

    const login_request = new LoginRequest();
    let is_form_ready = false;

    let form_data = [
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
            login_request.do(data => {
                if (data.token !== undefined) {
                    cordelia_storage.Token = data.token;
                    window.queueMicrotask(() => push('/courses'));
                }
            });
        }
    }

    const aside_img_url = "/resources/Fotografias/Corde-164-original.webp";
</script>

<CordeliaPants>
    <div slot="form" id="clp-login-form">
        <h2 class="page-title">iniciar sesión</h2>
        <div id="clp-lf-fields-container">
            {#each form_data as field}
                <div class="clp-lf-fc-field-wrapper">
                    <Input
                        field_data={field}
                        isClear={true}
                        isSquared={true}
                        input_color="var(--dark-light-color)"
                        input_dark_color="var(--theme-color)"
                        input_label={field.name}
                        onEnterPressed={verifyLoginForm}
                        onBlur={verifyLoginForm}
                    />
                </div>
            {/each}
        </div>
        <div id="clp-lf-form-controls">
            <button on:click={login} id="clp-lf-login-btn" class="full-btn">Iniciar sesion</button>
            <button on:click={() => push("/signup")} id="clp-lf-google-btn" class="full-btn">Google</button>
            <div id="clp-lf-create-account">
                <a href="/signup" use:link>Crear cuenta</a>
            </div>
            <div id="clp-lf-forgot-password">
                <a href="/password" use:link>Olvidé mi contraseña</a>
            </div>
        </div>
    </div>
</CordeliaPants>


<style>
    /* DEBUG */
    /* * {
        border: 1px solid red;
    } */


    #clp-login-form {
        width: 75%;
    }

    #clp-lf-fields-container .clp-lf-fc-field-wrapper{
        margin: var(--spacing-h3) 0;
    }

    #clp-lf-form-controls {
        display: grid;
        height: 20%;
        grid-template: repeat(2, 1fr) / repeat(2, 1fr);
        gap: var(--spacing-3) var(--spacing-3);
    }

    #clp-lf-create-account {
        grid-area: 2 / 1 / 3 / 2;
    }
    
    #clp-lf-forgot-password {
        grid-area: 2 / 2 / 3 / 3;
        text-align: right;
        font-weight: lighter;
        padding: 0 var(--spacing-2) 0 0;
    }

    #clp-lf-google-btn {
        display: none;
    }
    
    @media only screen and (max-width: 768px) {
        #clp-login-form {
            box-sizing: content-box;
            padding: var(--spacing-1) 0;
            width: 90%;
        }

        #clp-lf-form-controls {
            grid-template: auto / repeat(1, 1fr);
        }

        #clp-lf-form-controls * {
            width: 80%;
        }

        #clp-lf-forgot-password {
            text-align: left;
        }
    }
</style>

