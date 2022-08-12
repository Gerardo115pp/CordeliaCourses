<script>
    import FieldData, { verifyFormFields } from '../../libs/FieldData';
    import { PasswordRecoveryRequest } from '../../libs/HttpRequests';
    import Input from '../../components/Input.svelte';
    import CordeliaPants from '../../components/PantsBackground.svelte';
    import { push } from 'svelte-spa-router';

    const password_recovery_request = new PasswordRecoveryRequest();
    let is_form_ready = false;

    const form_data = [
        new FieldData('customer_email', /[^;\'\s\n]/, 'Correo electronico', 'email')
    ]

    // Link FormData to login_request
        $: password_recovery_request.email = form_data[0].getFieldValue();
    // 

    const verifyLoginForm = () => {
        let is_valid = verifyFormFields(form_data);
        is_form_ready = is_valid;
        form_data = [...form_data];
    }

    const login = () => {
        if (is_form_ready) {
            password_recovery_request.do();
        }
    }

    const aside_img_url = "/resources/Fotografias/Corde-164-original.webp";
</script>

<CordeliaPants>
    <div slot="form" id="prf-pw-recovery-form">
        <h2 class="page-title">¿OLVIDASTE TU CONTRASEÑA?</h2>
        <h3 class="password-page-subtitle">No te preocupes, te enviaremos un link para reestablecerla</h3>
        <div id="prf-lf-fields-container">
            {#each form_data as field}
                <div class="prf-lf-fc-field-wrapper">
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
        <div id="prf-lf-form-controls">
            <button on:click={() => push('/login')} id="prf-lf-login-btn" class="full-btn">Enviar link</button>
        </div>
    </div>
</CordeliaPants>


<style>
    /* DEBUG */
    /* * {
        border: 1px solid red;
    } */


    #prf-pw-recovery-form {
        width: 75%;
    }

    .password-page-subtitle {
        font-family: var(--font-texts);
        font-size: var(--font-size-3);
        color: var(--dark-light-color);
        text-transform: none;
    }

    #prf-lf-fields-container .prf-lf-fc-field-wrapper{
        margin: var(--spacing-h3) 0;
    }

    #prf-lf-form-controls {
        display: grid;
        width: 60%;
        height: 20%;
        margin-top: var(--spacing-h2);
        grid-template: repeat(2, 1fr) / repeat(2, 1fr);
        gap: var(--spacing-3) var(--spacing-3);
    }
    
</style>

